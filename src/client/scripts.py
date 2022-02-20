import glob, os, shutil
from pathlib import Path
from crud import get_scripts, set_scripts


def get_name_from_path(config, file_name):
    name = file_name.replace("\\", "/").replace(config["SRC_DIR"], "").replace(".lua", "").strip("/").strip()
    return name


def get_all_script_paths(config):
    return glob.glob(f"{config['SRC_DIR']}**/*.lua", recursive=True)


def get_source_dir(config):
    cwd = Path(os.getcwd())
    return cwd / config["SRC_DIR"]


def init_script_dir(config):
    print(f"No existing scripts are present, initializing source directory.")
    main = """-- main

local has_reported = false

function main()
    if not has_reported then
        print("AI scripting is alive :)")
        has_reported = true
    end
end"""
    with open(get_source_dir(config) / "main.lua", "w") as f:
        f.write(main)


def download_scripts(config, account_id, overwrite):
    files = glob.glob(f"{Path(config['SRC_DIR'])}**/*.lua", recursive=True)

    if len(files) == 0 or overwrite:
        msg = "no existing scripts are present" if len(files) == 0 else "overwrite mode is active"
        print(f"Initializing local folder with current scripts as {msg}.")

        scripts = get_scripts(config["API_HOST"], account_id)

        src_dir = get_source_dir(config)

        print("Wiping the source directory as part of overwrite process.")
        shutil.rmtree(src_dir)

        for script in scripts:
            parent_folder = src_dir / "/".join(script["name"].split("/")[:-1])

            if not os.path.exists(parent_folder):
                os.makedirs(parent_folder)

            with open(src_dir / f'{script["name"]}.lua', "w") as f:
                f.write(script["script"])

        print(f"Added {len(scripts)} scripts.")
    else:
        print("Nothing to do as script files exist and overwite mode is disabled.")


def upload_scripts(config, script_file_paths, account_id, is_complete):
    scripts = []

    for script_file in script_file_paths:
        if not os.path.exists(script_file):
            print(f"Could not upload {script_file}, file no longer exists.")
            continue
        with open(script_file) as f:
            name = get_name_from_path(config, script_file)
            f.seek(0)
            script = f.read()
            scripts.append({"accountId": account_id, "script": script, "name": name})

    set_scripts(config["API_HOST"], scripts, account_id, is_complete)
