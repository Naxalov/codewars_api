from codewars import User

from datetime import datetime
from collections import defaultdict

def daily_completed_task_histogram(data):
    """
    Given a list of task dictionaries (each having a 'completedAt' field),
    return a histogram of completed tasks grouped by day (YYYY-MM-DD) and
    by hour (0-23).
    
    :param data: list of dictionaries, each with at least a 'completedAt' field
                 in ISO 8601 format (e.g., '2025-01-08T06:09:32.508Z')
    :return: A dictionary where:
             - keys:   'YYYY-MM-DD' strings
             - values: a list of 24 integers [count_0, count_1, ... count_23]
    """
    # This dictionary will map day_string -> [24-hour histogram].
    # For example: histograms["2025-01-08"] = [0, 0, 0, ..., 0]
    histograms = defaultdict(lambda: [0]*24)
    
    for task in data:
        completed_at_str = task.get('completedAt')
        if not completed_at_str:
            continue
        
        # Parse the completedAt string into a datetime object
        # Example "completedAt": "2025-01-08T06:09:32.508Z"
        # We can strip off the trailing 'Z' if present and parse the rest.
        datetime_str = completed_at_str.replace('Z', '')
        
        try:
            # Python’s strptime can parse microseconds if we use %f for fractional seconds
            completed_dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            # Fallback if there are no fractional seconds
            completed_dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
        
        # Create a day string in "YYYY-MM-DD" format
        day_str = completed_dt.strftime("%Y-%m-%d")
        hour_of_day = completed_dt.hour
        
        # Increase the count for that day, that hour
        # Note that our defaultdict is a fresh [0]*24 for each new day
        histograms[day_str][hour_of_day] += 1

        # Convert the defaultdict back to a regular dictionary
    histograms = dict(histograms)

    return histograms





    
"""
id,fullname,username
1,Ahror Hasanov,Akhror_Khasanov
2,Abdiraxmonov G'anijon,Ganijon
3,Elmurodov Ziyodullo,elmurodov
3,DILMUROD MAMARAJABOV,Dilmurodddd
5,Kamronbek BG,KamronbekBG
6,Nuraliyev Akobir,
"""

# Example usage
user = User('elmurodov', 'Akhror_Khasanov')
data = user.get_completed()['data']

histogram = daily_completed_task_histogram(data)
from pprint import pprint
print(histogram)
