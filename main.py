from codewars import User , Task

user = User('Kamoliddin-Otamurodov')
task = Task('Kamoliddin-Otamurodov')

print(user.check_user())
print(user.get_id())
print(user.get_username())
print(user.get_name())
print(user.get_honor())
print(user.get_clan())
print(user.get_leadpos())
print(user.get_skills())
print(user.get_rank())
print(user.get_total())

print(task.get_task_bydate("2023-12-03"))