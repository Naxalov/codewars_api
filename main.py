from codewars import User
import csv

# Read data from csv file
with open('codewars.csv') as csv_file:
    # Read data from csv file and skip header
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skip header
    next(csv_reader)
    for row in csv_reader:
        username = row[2]
        user = User(username)
        print(user.get_total())
    