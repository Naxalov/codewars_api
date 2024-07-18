import requests
from datetime import datetime
class User:

    def __init__(self, username: str):
        url = f'https://www.codewars.com/api/v1/users/{username}'
        url_completed = f'https://www.codewars.com/api/v1/users/{username}/code-challenges/completed'
        data = requests.get(url=url).json()
        self.username = username
        self.data = data
        data_pages = requests.get(url=url_completed).json()
        pages = data_pages['totalPages']
        data_problems = []
        for page in range(pages):
            url_pages = f'https://www.codewars.com/api/v1/users/allamurodxakimov/code-challenges/completed?page={page}'
            data_p = requests.get(url=url_pages).json()
            for problem in data_p['data']:
                data_problems.append(problem)
        self.problems = data_problems
    
    def get_name(self):
        return f"Name: {self.data['name']}"
    def get_clan(self):
        return f"Clan: {self.data['clan']}"
    def get_rank(self):
        return f"Ranks: {self.data['ranks']['overall']['rank']} \nRank name: {self.data['ranks']['overall']['name']}"
    def get_totalcomplated(self):
        return f"totalCompleted: {self.data['codeChallenges']['totalCompleted']}"
    def codewars_check_completedAt(self, day: int, month: int, year: int):
        # date_now = datetime.now()
        # day, month, year = date_now.day, date_now.month, date_now.year
        c = 0
        for item in self.problems:
            date_old = datetime.fromisoformat(item['completedAt'])
            day2, month2, year2 = date_old.day, date_old.month, date_old.year
            if day==day2 and month==month2 and year==year2:
                c+=1
        return f"completedAt day: {c}"
    