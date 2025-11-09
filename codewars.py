import requests
import csv
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

    def __init__(self, users: list):
        self.users = []
        for user in users:
            user_obj = User(user["username"], user["fullname"])
            print(f"{user['fullname']} added")
            self.users.append(user_obj)

    def add_user(self, username):
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
        user_count = {"users_count": 0}
        for user in self.users:
            user_count["users_count"] += 1
        return user_count

    def get_total_daily(self):
        """
        This method returns the total number of completed for all users by daily
        """
        user = {
            "username": "",
            "name": "",
            "total_completed": 0,
        }
        result = []
        for user in self.users:
            user = {
                "name": user.fullname,
                "username": user.username,
                "total_completed": user.get_daily(),
            }
            result.append(user)
        result = sorted(result, key=lambda x: x["total_completed"], reverse=True)
        return result

    def get_total_weekly(self):
        """
        This method returns the total number of completed for all users by weekly
        """
        user = {
            "username": "",
            "name": "",
            "total_completed": 0,
        }
        result = []
        for user in self.users:
            user = {
                "name": user.fullname,
                "username": user.username,
                "total_completed": user.get_weekly(),
            }
            result.append(user)
        result = sorted(result, key=lambda x: x["total_completed"], reverse=True)
        return result

    def get_total_date(self, date_type):
        """
        This method returns the total number of completed for all users by date type (daily, weekly, monthly)
        """

        now = datetime.now()

        user_data = {"username": "", "fullname": "", "total_completed": 0}
        result_users = []
        for user in self.users:
            url_pages = f"https://www.codewars.com/api/v1/users/{user['username']}/code-challenges/completed"
            data_Com = requests.get(url=url_pages).json()
            count = 0
            if date_type == "daily":
                day, month, year = now.day, now.month, now.year
                for item in data_Com["data"]:
                    date_old = datetime.fromisoformat(item["completedAt"])
                    day_at, month_at, year_at = (
                        date_old.day,
                        date_old.month,
                        date_old.year,
                    )
                    if day_at == day and month_at == month and year_at == year:
                        count += 1

            elif date_type == "weekly":
                now_second = now.timestamp()
                for item in data_Com["data"]:
                    date_old = datetime.fromisoformat(item["completedAt"])
                    date_old_second = date_old.timestamp()
                    if abs(now_second - date_old_second) <= 7 * 24 * 3600:
                        count += 1

            elif date_type == "monthly":
                now_second = now.timestamp()
                for item in data_Com["data"]:
                    date_old = datetime.fromisoformat(item["completedAt"])
                    date_old_second = date_old.timestamp()
                    if abs(now_second - date_old_second) <= 30 * 24 * 3600:
                        count += 1
            user_data = {
                "username": user["username"],
                "fullname": user["fullname"],
                "total_completed": count,
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
            "username": "",
            "total_completed": 0,
            "name": "",
        }
        result = []
        for username in self.users:
            user = User(username)
            user = {
                "username": username,
                "total_completed": user.get_total(),
            }
            result.append(user)
        result = sorted(result, key=lambda x: x["total_completed"], reverse=True)
        return result

    def export_total_completed_to_csv(self):
        """
        This method exports the total number of completed for all users to a csv file
        """

        with open("codewars_total.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "Username", "Completed Tasks"])
            for id, username in enumerate(self.users):
                user = User(username)
                writer.writerow([id + 1, username, user.get_total()])
        return "OK"


class User:
    """
    User class
    """

    def __init__(self, username, base_url="https://www.codewars.com/api/v1/users/"):
        self.base_url = base_url
        self.data, self.full_url = self.get_user_data(username)

        self.set_fullname()
        self.set_username()

        self.completed = self.get_all_completed()
        self.total_pages = 0

    def get_user_data(self, username=None) -> tuple:
        """
        Get user data from the Codewars API.
        Args:
            username (str, optional): The Codewars username to retrieve data for. Defaults to None.
        Returns:
            tuple: A tuple containing:
                - dict: User data retrieved from the API
                - str: The full URL used for the request
        Raises:
            ValueError: If the username is not found (status code != 200)
        """
        full_url = f"{self.base_url}{username}"
        r = requests.get(url=full_url)
        if r.status_code != 200:
            raise ValueError(f"Username {username} not found")

        data = r.json()
        return data, full_url

    def get_all_completed(self) -> None:
        """
        Get number of completed kata

        returns(int): number of completed kata
        """
        URL = f"{self.full_url}/code-challenges/completed"
        r = requests.get(url=URL)

        data = r.json()

        total_pages = data["totalPages"]

        for page in range(1, total_pages):
            URL_page = f"{self.full_url}/code-challenges/completed?page={page}"
            r_page = requests.get(url=URL_page)
            data_page = r_page.json()
            data["data"].extend(data_page["data"])

        self.all_data = data

    def set_fullname(self) -> None:
        """
        Set fullname

        args:
            fullname(str): fullname
        """
        fullname = self.data.get("name")
        self.fullname = fullname

    def set_username(self) -> None:
        """
        Set username from API data

        raises:
            ValueError: if username is not valid
        """
        username = self.data.get("username")
        self.username = username

    def get_total(self) -> int:
        """
        Get total number of completed kata

        returns(int): total number of completed kata
        """
        if self.check_username() == True:
            return self.data["codeChallenges"]["totalCompleted"]
        return False

    def get_completed_by_date(self, date) -> int:
        """
        Get number of completed kata by date

        args:
            date(str): date
        returns(int): number of completed kata
        """
        day, month, year = date
        data_problems = self.all_data["data"]
        count = 0
        for item in data_problems:
            date_old = datetime.fromisoformat(item["completedAt"])
            day2, month2, year2 = date_old.day, date_old.month, date_old.year
            if day == day2 and month == month2 and year == year2:
                count += 1
        return count

    def get_monthly(self) -> int:
        """
        Get number of completed kata last month

        returns(int): number of completed kata
        """
        now = datetime.now()
        now_second = now.timestamp()
        count = 0
        for item in self.completed["data"]:
            date_old = datetime.fromisoformat(item["completedAt"])
            date_old_second = date_old.timestamp()
            if abs(now_second - date_old_second) <= 30 * 24 * 3600:
                count += 1
        return count

    def get_daily(self) -> int:
        """
        Get number of completed kata last day

        returns(int): number of completed kata
        """
        today = date.today()

        count = 0
        data = self.completed["data"]
        for item in data:
            # 2024, 8, 2
            completed_at = datetime.fromisoformat(item["completedAt"])
            # Compare dates
            if today == completed_at.date():
                count += 1

        return count

    def get_weekly(self) -> int:
        """
        Get number of completed kata this week

        returns(int): number of completed kata
        """
        # Get current week date
        current_date = datetime.now().date()
        week_date = current_date - timedelta(days=datetime.now().weekday())

        data = self.completed["data"]
        total = 0  # Total number of completed kata in current week
        for item in data:
            completed_at = datetime.fromisoformat(item["completedAt"])
            # Check if completed date is in current week
            if week_date <= completed_at.date() <= current_date:
                total += 1

        return total

    def get_honor(self) -> int:
        """
        Total honor points earned by user

        returns(int): total honor points
        """
        return self.data.get("honor")

    def get_clan(self) -> str:
        """
        Get clan name

        returns(str): clan name
        """
        return self.data.get("clan")

    def get_leaderboard_position(self) -> int:
        """
        Get leaderboard position

        returns(int): leaderboard position
        """
        return self.data.get("leaderboardPosition")

    def get_skills(self) -> list:
        """
        Get list of user programming skills

        returns(list): list of porgramming languages
        """
        return self.data.get("skills")
