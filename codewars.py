import requests
class User:

    def __init__(self, username: str):
        url = f'https://www.codewars.com/api/v1/users/{username}'
        data = requests.get(url=url).json()
        self.username = username
        self.data = data
    
    def get_name(self):
        return f"Name: {self.data['name']}"
    def get_clan(self):
        return f"Clan: {self.data['clan']}"
    def get_rank(self):
        return f"Ranks: {self.data['ranks']['overall']['rank']} \nRank name: {self.data['ranks']['overall']['name']}"
    def get_totalcomplated(self):
        return f"totalCompleted: {self.data['codeChallenges']['totalCompleted']}"
    