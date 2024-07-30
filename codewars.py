import requests

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
        if User(username).check_username()==True:
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
        l={}
        for i in self.users:
            get_total=User(i).get_total()
            l[i]=get_total
        return l


    def export_total_completed_to_csv(self):
        """
        This method exports the total number of completed for all users to a csv file
        """

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
