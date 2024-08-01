from codewars import User, Users
import csv

users = []
# Read data from csv file
with open('codewars.csv') as csv_file:
    # Read data from csv file and skip header
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skip header
    next(csv_reader)
    users = []
    for row in csv_reader:
        username = row[2]
        fullname = row[1]
        user = User(username)
        # print(user.get_completed_by_date((29, 7, 2024)))
        print(user.get_weekly())
        # print(user.get_monthly())

        # print(f'{fullname} : {user.get_total()}')
        # print(user.get_name())
        # users.append(username)
# user_all = Users(users)
# print(user_all.get_total_completed())
# print(user_all.get_num_users())
# print(user_all.export_total_completed_to_csv())
# completed = user_all.get_total_completed()
# print(completed)
# Convert to CSV
# with open('results.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['fullname','username', 'total_completed'])
#     for user in completed:
#         print(user)
#         writer.writerow([user['name'], user['username'], user['total_completed']])
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
