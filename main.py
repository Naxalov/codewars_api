from codewars import User, Users
from pprint import pprint
import csv

# users = []
# Read data from csv file
path ='python_2.csv'
users = [

]

with open(path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append({
            'username': row['username'],
            'fullname': row['fullname']
        })
        
print(users)
users = Users(users)

pprint(users.get_total_daily())


# user = User('elmurodov')
# pprint(user.get_completed())
# print(user.get_daily())