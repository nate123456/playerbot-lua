import argparse, glob, time, os, queue
from pathlib import Path

from config import get_config
from logs import setup_log_streaming
from crud import get_account_id, get_scripts, set_scripts
from scripts import download_scripts, upload_scripts, get_all_script_paths, init_script_dir
from watch import FileChangeProducerThread, FileChangeConsumerThread


def main():

    config = get_config()

    # config was initialized or not valid, user must configure.
    if not config:
        return

    parser = argparse.ArgumentParser(description="Manage playerbot script development")

    parser.add_argument("-logs", action="store_true", help="Listen for log output from running playerbot scripts")
    parser.add_argument("-watch", action="store_true", help="Watch for and automatically deploy script changes")
    parser.add_argument("-overwrite", action="store_true", help="Overwrite with current scripts from server")
    parser.add_argument("-deploy", action="store_true", help="Deploy all scripts to the server")

    args = parser.parse_args()

    account_id = get_account_id(config["API_HOST"], config["TOKEN"])

    if account_id == 0:
        error_str = f"Error: provided token '{config['TOKEN'].upper()}' is not valid or has expired.\n"
        error_str = error_str + "Use '.bot ai get token' in-game to get a valid token."
        print(error_str)
        return

    if args.logs:
        setup_log_streaming(account_id, config)

    cwd = Path(os.getcwd())
    src_dir = cwd / config["SRC_DIR"]

    if not os.path.exists(src_dir):
        print(f"Source directory does not exist. Creating '{config['SRC_DIR']}'.")
        os.makedirs(src_dir)

    if args.deploy or args.watch:
        msg = " to initialize file watching" if args.watch else ""
        print(f"Beginning full script deployment{msg}.")
        files = get_all_script_paths(config)
        upload_scripts(config, files, account_id, True)
    else:
        download_scripts(config, account_id, args.overwrite)

    p = None
    c = None
    
    if args.watch:
        q = queue.Queue()
        p = FileChangeProducerThread(config, account_id, q)
        c = FileChangeConsumerThread(config, account_id, q)

        p.start()
        c.start()
        print(f"File watcher ready.")

    if len(get_all_script_paths(config)) == 0:
        init_script_dir(config)

    if args.logs or args.watch:
        print("Press CTRL+C to exit.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            p.stop()
            c.stop()

    print("All tasks complete.")


if __name__ == "__main__":
    main()
