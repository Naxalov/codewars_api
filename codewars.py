import requests
import csv
input_file='codewars.csv'
output_file='codewars.csv'

class Users:
    """
    Users class
    """
    def __init__(self,users:list):
        self.users = users
    def add_user(self,username):
        """
        This method adds a new user to the list of users

        args:
            username(str): username
        returns:
            total(int): total number of users
        """
        self.users.append(username)
        return len(self.users)

    def get_num_users(self):
        """
        This method returns the total number of users

        returns:
            total(int): total number of users
        """
        return len(self.users)

    def get_total_completed(self):
        """
        This method returns the total number of completed for all users

        returns:
            result(dict): total number of completed for all users
        """
        a = 0
        for username in self.users:
            user = User(username)
            a += user.get_total()
        return {"total_completed" : a}
    def export_total_completed_to_csv(self):
        """
        This method exports the total number of completed for all users to a csv file

        args:
            input_file(str): name of the input csv file
            output_file(str): name of the output csv file
        """
        total_completed = self.get_total_completed()["total_completed"]

        # Read the input CSV file
        with open(input_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]

        # Add the new column to the header
        header = data[0]
        header.append('total_completed')

        # Add the total_completed value to the first row
        data[1].append(total_completed)

        # Add empty values to the rest of the rows for the new column
        for row in data[2:]:
            row.append('')

        # Write the updated data to the output CSV file
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

class User:
    """
    User class
    """
    def __init__(self,username):
       self.data = requests.get(f'https://www.codewars.com/api/v1/users/{username}').json() 
       if self.check_username():
           self.username = username
       else:
           self.username = None

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
        return self.data['leaderboardPosition']
    def get_skills(self):
        """
        Get list of user programming skills

        returns(list): list of porgramming languages
        """
        return self.data['skills']
