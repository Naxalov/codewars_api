from codewars import User, Users
import csv

users = []
# Read data from csv file
path ='ai_2024_1.csv'
with open(path) as csv_file:
    # Read data from csv file and skip header
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skip header
    next(csv_reader)
    for row in csv_reader:
        username = row[2]
        users.append(username)
    

from pprint import pprint
print(users)
grpup = Users(users)
completed = grpup.get_total_completed()
print(completed)
# Convert to CSV
with open('results.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['username', 'total_completed'])
    for user in completed:
        print(user)
        writer.writerow([user['username'], user['total_completed']])
