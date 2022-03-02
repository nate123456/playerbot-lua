import os, json
from pathlib import Path
import yaml

default_config = {
    "TOKEN": "ABC123",
    "API_HOST": "http://localhost:5000/",
    "LOG_HOST": "http://localhost:1883/",
    "SRC_DIR": "src/",
    "WATCHER_DEPLOY_THROTTLE_MS": 100,
}


def get_config():
    cwd = Path(os.getcwd())
    config_path = cwd / "config.yml"
    config = None

    if os.path.exists(config_path):
        with open(config_path) as f:
            try:
                config=yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)

    if not config:
        print("No configuration detected, creating initial config file. Please configure as appropriate.")

        with open(config_path, "w") as yaml_file:
            yaml.dump(default_config, yaml_file, default_flow_style=False)

        return

    if not config["API_HOST"]:
        print("Configuration must provide the 'API_HOST' configuration value.")
        return

    if type(config["API_HOST"]) is not str:
        print("'API_HOST' must be a string.")
        return

    if not config["LOG_HOST"]:
        print("Configuration must provide the LOG_HOST configuration value.")
        return

    if type(config["LOG_HOST"]) is not str:
        print("'LOG_HOST' must be a string.")
        return

    if not config["TOKEN"]:
        print("Configuration must provide the 'TOKEN' configuration value.")
        return

    if type(config["TOKEN"]) is not str:
        print("'TOKEN' must be a string.")
        return

    if len(config["TOKEN"]) != 6:
        print(f"'TOKEN' must be 6 alpha-numeric characters. Provided token: '{config['TOKEN']}'")
        return

    if not config["SRC_DIR"]:
        print("Configuration must provide the SRC_DIR configuration value.")
        return

    if type(config["SRC_DIR"]) is not str:
        print("'SRC_DIR' must be a string.")
        return

    return config
