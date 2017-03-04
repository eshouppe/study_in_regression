post_request_template = {
    "q": {
        "_text_any":{
            "patent_abstract": 1
            }
        },
        "f": 1,
        "s": [{"patent_date":"desc"}],
        "o": {
            "per_page": 100
        }
    }