import requests

URL = "https://www.codewars.com/api/v1/users/"

 
class User:
    def __init__(self , username):
        self.username = username
        self.data = requests.get(URL + self.username).json()

    def check_user(self):
        if "username" in self.data:
            return True
        return "Error"
    
    def get_id(self):
        if "id" in self.data:
            return self.data.get('id')
        return "Error"

    def get_username(self):
        if "username" in self.data:
            return self.data.get('username')
        return "Error"
    
    def get_name(self):
        if "name" in self.data:
            return self.data.get('name')
        return "Error"

    def get_honor(self):
        if "honor" in self.data:
            return self.data.get('honor')
        return "Error"

    def get_clan(self):
        if "clan" in self.data:
            return self.data.get('clan')
        return "Error"

    def get_leadpos(self):
        if "leaderboardPosition" in self.data:
            return self.data.get('leaderboardPosition')
        return "Error"

    def get_skills(self):
        if "skills" in self.data:
            return self.data.get('skills')
        return "Error"

    def get_langs(self):
        if "languages" in self.data:
            return self.data.get('languages')
        return "Error"
        

    def get_rank(self):
        if "ranks" in self.data:
            return self.data.get('ranks')
        return "Error"

    def get_total(self):
        if "codeChallenges" in self.data:
            return self.data.get('codeChallenges').get('totalCompleted')
        return "Error"


class Task:
    def __init__(self  ,  username):
        self.username = username
        self.data = requests.get(URL + self.username + "/code-challenges/completed").json()["data"]

    def get_task_bydate(self , date):
        a = []
        for i in self.data:
            if i.get("completedAt")[:10] == date:
                a.append(i)
        return a