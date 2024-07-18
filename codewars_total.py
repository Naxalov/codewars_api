import requests

class User:
    """
    User class
    """
    def __init__(self,user):
        url = f"https://www.codewars.com/api/v1/users/{user}/code-challenges/completed?page"
        self.user = user
        self.data = requests.get(url=url).json()
    def get_completed(self):
        s=0
        for i in self.data['data']:
            if i["completedAt"][:10]=="2024-07-11":
                s+=1
        return s