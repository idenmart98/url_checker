import requests

def get_code(url):
    try:
        r = requests.get(url)
        return r.status_code
    except requests.exceptions.ConnectionError:
        return 0