import requests

class User:
    """
    User class
    """
    def __init__(self,user):
        url = f"https://www.codewars.com/api/v1/users/{user}"
        self.user = user
        self.data = requests.get(url=url).json()
    def get_total(self):
        return f"totalCompleted: {self.data['codeChallenges']['totalCompleted']}"
