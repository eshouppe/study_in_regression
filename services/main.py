class PatentQuestions:
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
                    "per_page": 100
                }
            }


    def num_citations_by_patent(self):
        """Count how many citations a patent has.
        Possible regression methods are poisson, OLS,
        ridge, and lasso."""
        pass

    def num_citations_of_patent(self):
        """Count how many patents will cite this patent.
        Possible regression methods are poisson, OLS,
        ridge, and lasso."""
        pass

    def patent_approval_probability(self):
        """Probability that a patent will be approved.
        Possible regression method is logistic."""
        pass

    def num_days_to_approve(self):
        """Number of days between submission and approval.
        Possible regression methods are poisson, OLS,
        ridge, and lasso."""
        pass

    def num_patents_approved_by_month(self):
        """Monthly trend in volume of patents approved.
        Possible regression methods are poisson, OLS,
        ridge, and lasso."""
        pass
