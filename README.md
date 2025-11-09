# Codewars API

A Python library for interacting with the Codewars API to track and analyze user progress, kata completion statistics, and generate various reports.

## Features

- Fetch user data from Codewars API
- Track daily, weekly, and monthly kata completions
- Generate completion histograms
- Export data to CSV files
- Analyze solved katas for specific kata IDs
- Support for multiple users

## Classes

### Users

Main class for managing multiple Codewars users and generating aggregate statistics.

#### Constructor
```python
Users(users: list[str])
```
- `users`: List of dictionaries containing `username` and `fullname` keys

#### Methods

##### Data Retrieval
- `get_total_daily()` - Get daily completion counts for all users
- `get_total_weekly()` - Get weekly completion counts for all users
- `get_total_date(date_type)` - Get completion counts by date type ("daily", "weekly", "monthly")
- `get_total_completed()` - Get total completion counts for all users
- `get_total_daily_completed_histogram()` - Get daily completion histograms for all users

##### Export Methods
- `export_total_completed_to_csv(file_path)` - Export total completions to CSV
- `export_total_daily_completed_histogram_to_csv(file_path)` - Export daily histograms to CSV
- `export_total_count_solved_katas_by_ids(kata_ids, file_path)` - Export solved kata counts to CSV

##### User Management
- `add_user(username)` - Add a new user to the collection

### User

Class for individual Codewars user data and statistics.

#### Constructor
```python
User(username: str, full_name: str = None, base_url: str = "https://www.codewars.com/api/v1/users/")
```

#### Methods

##### Completion Statistics
- `get_total()` - Get total number of completed katas
- `get_daily()` - Get number of katas completed today
- `get_weekly()` - Get number of katas completed this week
- `get_monthly()` - Get number of katas completed in the last 30 days
- `get_completed_by_date(date_str)` - Get completions for a specific date (YYYY-MM-DD format)

##### User Information
- `get_honor()` - Get total honor points
- `get_clan()` - Get clan name
- `get_leaderboard_position()` - Get leaderboard position
- `get_skills()` - Get list of programming skills

##### Data Analysis
- `daily_completed_task_histogram()` - Generate daily completion histogram
- `count_solved_katas_by_ids(kata_ids)` - Count how many specific katas the user has solved

## Usage Examples

### Basic Usage

```python
from codewars import Users, User

# Create a single user
user = User("username")
print(f"Total completed: {user.get_total()}")
print(f"Daily completed: {user.get_daily()}")
print(f"Weekly completed: {user.get_weekly()}")

# Create multiple users
users_data = [
    {"username": "user1", "fullname": "John Doe"},
    {"username": "user2", "fullname": "Jane Smith"}
]
users = Users(users_data)

# Get daily statistics for all users
daily_stats = users.get_total_daily()
print(daily_stats)
```

### Export Data

```python
# Export total completions to CSV
users.export_total_completed_to_csv("output/completions.csv")

# Export daily histograms to CSV
users.export_total_daily_completed_histogram_to_csv("output/daily_histogram.csv")

# Check specific kata completion
kata_ids = ["kata1", "kata2", "kata3"]
users.export_total_count_solved_katas(kata_ids, "output/solved_katas.csv")
```

### Date-based Analysis

```python
# Get completions by different time periods
daily_data = users.get_total_date("daily")
weekly_data = users.get_total_date("weekly")
monthly_data = users.get_total_date("monthly")

# Get completions for specific date
user = User("username")
completions = user.get_completed_by_date("2024-08-02")
```

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Required packages:
- `requests` - For API calls
- `csv` - For CSV export functionality (built-in)
- `datetime` - For date handling (built-in)
- `collections` - For defaultdict (built-in)

## Error Handling

The library includes error handling for:
- Invalid usernames (raises `ValueError`)
- API connection issues
- Invalid date types in `get_total_date()` method

## Output Formats

### CSV Export Formats

#### Total Completions CSV
```
id,Username,Completed Tasks
1,user1,150
2,user2,120
```

#### Daily Histogram CSV
```
Date,user1,user2
2024-01-01,5,3
2024-01-02,2,4
```

#### Solved Katas CSV
```
id,Username,Solved Katas
1,user1,25
2,user2,18
```

## API Endpoints Used

- User data: `https://www.codewars.com/api/v1/users/{username}`
- Completed challenges: `https://www.codewars.com/api/v1/users/{username}/code-challenges/completed`

## License

This project is open source and available under the MIT License.