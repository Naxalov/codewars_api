import requests
from codewars_total import User

user = User('abdumajid_1')

# Get total completed kata
print(user.get_completed())