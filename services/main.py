"""Times square for app. The user selects a question, which can
be one of this module's functions. And then each question triggers
the steps needed to answer it"""

class PatentQuestions:
    def __init__(self):
        pass

    def num_citations_by_patent(self):
        """Count how many citations a patent has.
        Possible regression methods are poisson, OLS,
        ridge, and lasso."""
        query_fields = {"_gte":{"patent_date":"2010-01-01"}}
        result_fields = ['app_date', 'assignee_country', 'assignee_total_num_patents',
        'assignee_type', 'patent_num_combined_citations']


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
