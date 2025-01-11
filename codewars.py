import requests
import csv
from datetime import datetime, date, timedelta
from spire.doc import *
from spire.doc.common import *

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
        user_data = {
            'username':'',
            'name':'',
            'total_completed':0,
        }
        result = []
        for user in self.users:
            user_data={
                'name':user.fullname,
                'username':user.username,
                'total_completed':user.get_daily()
            }
            result.append(user_data)
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
            user_data={
                'name':user.fullname,
                'username':user.username,
                'total_completed':user.get_weekly()
            }
            result.append(user_data)
        result = sorted(result,key=lambda x:x['total_completed'],reverse=True)
        return result
    
    def get_total_monthly(self):
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
            user_data={
                'name':user.fullname,
                'username':user.username,
                'total_completed':user.get_monthly()
            }
            result.append(user_data)
        result = sorted(result,key=lambda x:x['total_completed'],reverse=True)
        return result
    
    def get_total_date(self,date_type):
        """
        This method returns the total number of completed for all users by date type (daily, weekly, monthly)
        """        
        
        result_users = []
        for user in self.users:
            total = 0
            if date_type == 'daily':
                total = user.get_daily()

            elif date_type == 'weekly':
                total = user.get_weekly()

            elif date_type == 'monthly':
                total = user.get_monthly()
            else:
                total = user.get_total()
            user_data = {
                "username": user.username,
                "fullname": user.fullname,
                "total_completed": total
            }      
            result_users.append(user_data)
        result_users = sorted(result_users,key=lambda x:x['total_completed'],reverse=True)
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
    
    def get_users_html_convert(self, user_data: list, result_image_path: str, type_completeAt: str):
        results = """"""
        for idx,user in enumerate(user_data):
            results += f"""
                <tr>
                    <td>{"🥇 "+user['fullname'].title() if idx==0 else "🥈 "+user['fullname'].title() if idx==1 else "🥉 "+user['fullname'].title() if idx==2 else str(idx+1)+'. '+user['fullname'].title()}</td>
                    <td>{user['total_completed']}</td>
                </tr>
                """
        html_file_str = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Codewars CompleteAt users</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div>
                <table>
                    <h1>IT Markazda codewars natijalari({type_completeAt})</h1>
                    <tr>
                        <th>Full Name</th>
                        <th>Total Completed</th>
                    </tr>
                    {results}
                </table>
            </div>
        </body>
        </html>
            
        """
        
        with open("index.html", "w", encoding="utf-8") as file_html:
            file_html.write(html_file_str)
            file_html.close()
        
        # Create a Document object
        document = Document()

        # Load an HTML file 
        document.LoadFromFile("index.html", FileFormat.Html, XHTMLValidationType.none)

        # Save the first page as an image stream
        imageStream = document.SaveImageToStreams(0, ImageType.Bitmap)

        # Convert the image stream as a PNG file
        with open(result_image_path,'wb') as imageFile:
            imageFile.write(imageStream.ToArray())
            document.Close()
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
        pages = self.completed['totalPages']
        day, month, year = date
        data_problems = []
        for page in range(pages):
            url_pages = f'https://www.codewars.com/api/v1/users/{self.username}/code-challenges/completed?page={page}'
            data_p = requests.get(url=url_pages).json()
            for problem in data_p['data']:
                data_problems.append(problem)
        total = 0
        for item in data_problems:
            date_old = datetime.fromisoformat(item['completedAt'])
            day2, month2, year2 = date_old.day, date_old.month, date_old.year
            if day==day2 and month==month2 and year==year2:
                total += 1
        return total  
    

    def get_daily(self):
        """
        Get number of completed kata last day

        returns(int): number of completed kata
        """
        today = date.today()
        total = 0
        data = self.completed['data']
        for item in data:        
            completed_at =datetime.strptime(item['completedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
            # Compare dates
            if today == completed_at.date():
                total += 1
          
        return total
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
            completed_at =datetime.strptime(item['completedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
            # Check if completed date is in current week
            if week_date <= completed_at.date() <= week_date + timedelta(days=7):
                total+=1
        
        return total
    
    def get_monthly(self):
        """
        Get number of completed kata last month

        returns(int): number of completed kata
        """
        monthly_date = datetime.now().date() - timedelta(days=datetime.now().day)
        data = self.completed['data']
        total = 0 # Total number of completed kata in current month
        for item in data:        
            completed_at =datetime.strptime(item['completedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
            # Check if completed date is in current month
            if monthly_date  <= completed_at.date() <= monthly_date +  timedelta(days=30):
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