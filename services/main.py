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


def num_citations_by_patent():
    """Count how many citations a patent has.
    Possible regression methods are poisson, OLS,
    ridge, and lasso."""
    pass

def num_citations_of_patent():
    """Count how many patents will cite this patent.
    Possible regression methods are poisson, OLS,
    ridge, and lasso."""
    pass

def patent_approval_probability():
    """Probability that a patent will be approved.
    Possible regression method is logistic."""
    pass

def num_days_to_approve():
    """Number of days between submission and approval.
    Possible regression methods are poisson, OLS,
    ridge, and lasso."""
    pass

def num_patents_approved_by_month():
    """Monthly trend in volume of patents approved.
    Possible regression methods are poisson, OLS,
    ridge, and lasso."""
    pass
