from codewars import User
import requests
user = User('abdumajid_1')

# Get total completed kata
# print(user.get_name())
# print(user.get_clan())
# print(user.get_totalcomplated())
# print(user.get_rank())
print(user.codewars_check_completedAt(day=19, month=7, year=2024))

