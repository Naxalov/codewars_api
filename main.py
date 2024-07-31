from codewars import User, Users
import csv

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
        print(f'{fullname} : {user.get_total()}')
        # print(user.get_name())
        users.append(username)
    user_all = Users(users)
    # print(user_all.get_total_completed())
    # print(user_all.get_num_users())
    print(user_all.export_total_completed_to_csv())