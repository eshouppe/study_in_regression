import requests


def make_post_req(self, payload):
    resp = requests.post(
        "http://www.patentsview.org/api/patents/query",
        json=payload
        )
        
    resp.raise_for_status()

    try:
        return resp.json()
    except ValueError:
        print("HTTP error")
        return "HTTP error"