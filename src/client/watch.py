import time, threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from crud import delete_scripts
from scripts import upload_scripts, get_name_from_path


class Handler(FileSystemEventHandler):
    def __init__(self, config, account_id, queue) -> None:
        super().__init__()
        self.config = config
        self.account_id = account_id
        self.queue = queue
        self.sends = {}

    def send_change(self, file_path, is_delete=False):
        if not file_path.endswith(".lua"):
            return

        if is_delete:
            self.queue.put({"is_delete": True, "file_path": file_path})
            return

        if file_path in self.sends:
            if time.time() - self.sends[file_path] < int(self.config["WATCHER_DEPLOY_THROTTLE_MS"]) / 1000:
                return

        self.queue.put({"is_delete": False, "file_path": file_path})
        self.sends[file_path] = time.time()

    def on_created(self, event):
        self.send_change(event.src_path)
        return super().on_created(event)

    def on_modified(self, event):
        self.send_change(event.src_path)
        return super().on_modified(event)

    def on_deleted(self, event):
        self.send_change(event.src_path, True)
        return super().on_deleted(event)

    def on_moved(self, event):
        self.send_change(event.src_path)
        return super().on_moved(event)


class FileChangeProducerThread(threading.Thread):
    def __init__(self, config, account_id, queue):
        super(FileChangeProducerThread, self).__init__()
        self.config = config
        self.account_id = account_id
        self.queue = queue
        self.go = True

    def run(self):
        event_handler = Handler(self.config, self.account_id, self.queue)
        observer = Observer()
        observer.schedule(event_handler, self.config["SRC_DIR"], recursive=True)
        observer.start()

        while self.go:
            time.sleep(0.01)

    def stop(self):
        self.go = False


class FileChangeConsumerThread(threading.Thread):
    def __init__(self, config, account_id, queue):
        super(FileChangeConsumerThread, self).__init__()

        self.config = config
        self.account_id = account_id
        self.queue = queue
        self.go = True

    def run(self):
        while self.go:
            if not self.queue.empty():
                item = self.queue.get()
                if item["is_delete"]:
                    delete_scripts(self.config["API_HOST"], [item["file_path"]], self.account_id)
                else:
                    upload_scripts(self.config, [item["file_path"]], self.account_id, False)

                name = get_name_from_path(self.config, item["file_path"])
                pretty_name = f"entrypoint script 'main'" if name == "main" else f"module '{name}'"
                print(f"{'Deployed removal of' if item['is_delete'] else 'Deployed'} {pretty_name}")
            else:
                time.sleep(0.01)

    def stop(self):
        self.go = False
