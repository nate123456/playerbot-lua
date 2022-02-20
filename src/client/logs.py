from paho.mqtt import client as mqtt_client


def on_message(client, userdata, msg):
    print(f"[LOG] {msg.payload.decode()}")


def setup_log_streaming(account_id: int, config):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("[LOG] Connected to Log stream.")
        else:
            print(f"[LOG] Failed to connect, return code:\n{rc}\n")

        client.subscribe(f"{account_id}/logs")
        print("[LOG] Log stream successfully initialized.")

    client = mqtt_client.Client(f"{account_id}")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config["LOG_HOST"])
