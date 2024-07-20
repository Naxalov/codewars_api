import requests
from pprint import pprint

b = 0
URL = f"http://www.codewars.com/api/v1/users/Kamoliddin-Otamurodov"
data = requests.get(URL).json()