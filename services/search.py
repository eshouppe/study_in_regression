import requests


class Search:
    def __init__(self):
        self.post_request_template = {
            "q": {
                "_text_any":{
                    "patent_abstract": 1
                    }
                },
                "f": 1,
                "s": [{"patent_date":"desc"}],
                "o": {
                    "per_page": 1000
                }
            }

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