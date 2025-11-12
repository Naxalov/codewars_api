from codewars import Users

# Read usernames from a CSV file
users = Users.from_csv("input/upwork.csv")
# list of kata IDs to check
users.add_kata_ids_by_file("input/kata_ids.csv")

# Export the count of solved katas for all users to a CSV file
users.export_solved_katas_count_to_csv(1)
