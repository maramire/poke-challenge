import requests

s = requests.Session()


def get(url):
    try:
        r = s.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    else:
        return r.json()
