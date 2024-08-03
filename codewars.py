import requests
import csv
from datetime import datetime, timedelta
from datetime import datetime, date, timedelta

class Users:
    """
    Users class
    user ={
        'username': username,
        'fullname': fullname,
        'total_completed': total_completed
    
    }
    """
    def __init__(self,users:list):
        self.users = []
        for user in users:
            user_obj = User(user['username'],user['fullname'])
            print(f"{user['fullname']} added")
            self.users.append(user_obj)

    def add_user(self,username):
        """
        This method adds a new user to the list of users

        args:
            username(str): username
        returns:
            total(int): total number of users
        """
        user = User(username)
        self.users.append(user)
        return len(self.users)

    def get_num_users(self):
        """
        This method returns the total number of users

        returns:
            total(int): total number of users
        """
        user_count = {
            'users_count': 0
        }
        for user in self.users:
            user_count['users_count'] += 1
        return user_count    

    def get_total_daily(self):
        """
        This method returns the total number of completed for all users by daily
        """
        user = {
            'username':'',
            'name':'',
            'total_completed':0,
        }
        result = []
        for user in self.users:
            user={
                'name':user.fullname,
                'username':user.username,
                'total_completed':user.get_daily()
            }
            result.append(user)
        result = sorted(result,key=lambda x:x['total_completed'],reverse=True)
        return result
    
    def get_total_weekly(self):
        """
        This method returns the total number of completed for all users by weekly
        """
        user = {
            'username':'',
            'name':'',
            'total_completed':0,
        }
        result = []
        for user in self.users:
            user={
                'name':user.fullname,
                'username':user.username,
                'total_completed':user.get_weekly()
            }
            result.append(user)
        result = sorted(result,key=lambda x:x['total_completed'],reverse=True)
        return result
    def get_total_date(self,date_type):
        """
        This method returns the total number of completed for all users by date type (daily, weekly, monthly)
        """
        
        now = datetime.now()
        
        user_data ={
        'username': '',
        'fullname': '',
        'total_completed': 0
        }
        result_users = []
        for user in self.users:
            url_pages = f"https://www.codewars.com/api/v1/users/{user['username']}/code-challenges/completed"
            data_Com = requests.get(url=url_pages).json()
            count = 0
            if date_type == 'daily':
                day, month, year = now.day, now.month, now.year
                for item in data_Com['data']:        
                    date_old = datetime.fromisoformat(item['completedAt'])
                    day_at, month_at, year_at = date_old.day, date_old.month, date_old.year
                    if day_at==day and month_at==month and year_at==year:
                        count += 1

            elif date_type == 'weekly':
                weekly_start = now - timedelta(days=7)
                weekly_start = weekly_start.strftime('%Y-%m-%d')
                weekly_start = datetime.strptime(weekly_start, '%Y-%m-%d')
                for item in data_Com['data']:        
                    date_end = datetime.strptime(item['completedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    if weekly_start <= date_end:
                        count += 1

            elif date_type == 'monthly':
                monthly_start = now - timedelta(days=30)
                monthly_start = monthly_start.strftime('%Y-%m-%d')
                monthly_start = datetime.strptime(monthly_start, '%Y-%m-%d')
                for item in data_Com['data']:        
                    date_end = datetime.strptime(item['completedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    if monthly_start <= date_end:
                        count += 1

            user_data = {
                "username": user['username'],
                "fullname": user['fullname'],
                "total_completed": count
            }      
            result_users.append(user_data)
        return result_users
    
    def get_total_completed(self):
        """
        This method returns the total number of completed for all users

        returns:
            result(list[dict]): total number of completed for all users
        """
        user = {
            'username':'',
            'total_completed':0,
            'name':'',
        }
        result = []
        for username in self.users:
            user = User(username)
            user={
                'username':username,
                'total_completed':user.get_total(),
            }
            result.append(user)
        result = sorted(result,key=lambda x:x['total_completed'],reverse=True)
        return result


    def export_total_completed_to_csv(self):
        """
        This method exports the total number of completed for all users to a csv file
        """
        
        with open('codewars_total.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'Username', 'Completed Tasks'])
            for id, username in enumerate(self.users):
                user = User(username)
                writer.writerow([id+1, username, user.get_total()])
        return 'OK'

class User:
    """
    User class
    """
    def __init__(self,username,fullname=None):
        self.data = requests.get(f'https://www.codewars.com/api/v1/users/{username}').json() 
        if fullname == None:
            raise ValueError(f'For {username} fullname is not specified')
        else:
            self.fullname = fullname

        if self.check_username():
            self.username = username
        else:
            raise ValueError(f'{username} is not a valid username')
        self.completed = self.get_completed() 
        self.total_pages = 0


    def get_completed(self):
        """
        Get number of completed kata

        returns(int): number of completed kata
        """
        URL = f'https://www.codewars.com/api/v1/users/{self.username}/code-challenges/completed'
        r = requests.get(url=URL)
        if r.status_code == 200:
            data = r.json()
       
        return data

    def check_username(self):
        """
        Check if username is valid

        returns(bool): True if username is valid
        """
        username=self.data.get('username')
        if username==None:
            return False
        return True
    
    def get_total(self):
        """
        Get total number of completed kata

        returns(int): total number of completed kata
        """
        if self.check_username() == True:
            return self.data["codeChallenges"]["totalCompleted"]
        return False

    def get_completed_by_date(self,date):
        """
        Get number of completed kata by date

        args:
            date(str): date
        returns(int): number of completed kata
        """
        url_completed = f'https://www.codewars.com/api/v1/users/{self.username}/code-challenges/completed'
        data_pages = requests.get(url=url_completed).json()
        pages = data_pages['totalPages']
        day, month, year = date
        data_problems = []
        for page in range(pages):
            url_pages = f'https://www.codewars.com/api/v1/users/{self.username}/code-challenges/completed?page={page}'
            data_p = requests.get(url=url_pages).json()
            for problem in data_p['data']:
                data_problems.append(problem)
        c = 0
        for item in data_problems:
            date_old = datetime.fromisoformat(item['completedAt'])
            day2, month2, year2 = date_old.day, date_old.month, date_old.year
            if day==day2 and month==month2 and year==year2:
                c+=1
        return c

  

    def get_monthly(self):
        """
        Get number of completed kata last month

        returns(int): number of completed kata
        """
        now = datetime.now()
        now_second = now.timestamp()
        url_pages = f'https://www.codewars.com/api/v1/users/{self.username}/code-challenges/completed'
        data_Com = requests.get(url=url_pages).json()
        c = 0
        for item in data_Com['data']:        
            date_old = datetime.fromisoformat(item['completedAt'])
            date_old_second = date_old.timestamp()
            if abs(now_second-date_old_second)<=30*24*3600:
                c+=1
        return c

    def get_daily(self):
        """
        Get number of completed kata last day

        returns(int): number of completed kata
        """
        today = date.today()
       
      
        c = 0
        data = self.completed['data']
        for item in data:        
            date_old = datetime.fromisoformat(item['completedAt'])
            # 2024, 8, 2
            completed_at =datetime.strptime(item['completedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
            # Compare dates
            if today == completed_at.date():
                c+=1
          
        return c
    def get_weekly(self):
            """
            Get number of completed kata last week

            returns(int): number of completed kata
            """
            # Get current week date
            week_date = datetime.now().date() - timedelta(days=datetime.now().weekday())

            data = self.completed['data']
            total = 0 # Total number of completed kata in current week
            for item in data:        
                completed_at = datetime.fromisoformat(item['completedAt'])
                # Check if completed date is in current week
                if week_date <= completed_at.date() <= week_date + timedelta(days=7):
                    total+=1
           
            return total

    def get_name(self):
        """
        Get username

        returns(str): username
        """
        if self.check_username() == True:
            return self.data["name"]
        return False
        
    def get_honor(self):
        """
        Total honor points earned by user

        returns(int): total honor points
        """
        return self.data.get('honor')

    def get_clan(self):
        """
        Get clan name

        returns(str): clan name
        """
        return self.data.get('clan')
    def get_leaderboard_position(self):
        """
        Get leaderboard position

        returns(int): leaderboard position
        """
        return self.get('leaderboardPosition')
    def get_skills(self):
        """
        Get list of user programming skills

        returns(list): list of porgramming languages
        """
        return self.get('skills')