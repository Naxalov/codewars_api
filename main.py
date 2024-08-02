from codewars import User, Users
from pprint import pprint
import csv

# Convert dict to CSV file
def dict_to_csv(data, path):
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# users = []
# Read data from csv file
group ='python_2'
users = [

]

with open(f'{group}.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append({
            'username': row['username'],
            'fullname': row['fullname']
        })
        
print(users)
users = Users(users)

daily=users.get_total_daily()
dict_to_csv(daily,f'{group}_daily.csv')


