import requests


def get_account_id(host, token):
    r = requests.get(f"{host}{'' if host.endswith('/') else '/'}scripts/{token}/")
    r.raise_for_status()

    if r.text:
        json = r.json()
        return json["accountId"]
    return 0


def get_scripts(host, account_id):
    r = requests.get(f"{host}{'' if host.endswith('/') else '/'}scripts/{account_id}/")
    r.raise_for_status()

    scripts = r.json()
    return scripts


def set_scripts(host, scripts, account_id, is_complete):
    data = {"accountId": account_id, "scripts": scripts, "isComplete": is_complete}

    headers = {"Content-type": "application/json", "Accept": "application/json"}

    r = requests.post(f"{host}{'' if host.endswith('/') else '/'}scripts/", json=data, headers=headers)
    r.raise_for_status()


def delete_scripts(host, script_names, account_id):
    data = {"accountId": account_id, "scriptNames": script_names}

    headers = {"Content-type": "application/json", "Accept": "application/json"}

    r = requests.post(f"{host}{'' if host.endswith('/') else '/'}scripts/", json=data, headers=headers)
    r.raise_for_status()
