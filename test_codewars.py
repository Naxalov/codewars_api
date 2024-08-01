from codewars import User
import datetime

def test_check_username():
    user = User('Naxalov')
    assert user.check_username() == False,' Username does not exist'
    user = User('naxalov')== True,'Correct username'

def test_get_total():
    user = User('naxalov')
    assert type(user.get_total()) == int, 'Should be number'

def test_get_name():
    """
    Test get_name function
    """
    user = User('Naxalov')
    assert user.get_name()==False
    user = User('naxalov')== "naxalov"
def test_get_honor():
    """
    Test get_honor function
    """
    user = User('naxalov')
    assert type(user.get_honor()) == int

def test_get_clan():
    """
    Test get_clan function
    """
    user = User('naxalov')
    assert user.get_clan()=='naxalov_2023'

def test_get_leaderboard_position():
    """
    Test get_leaderboard_position function
    """
    user=User("naxalov")
    assert type(user.get_leaderboard_position())==int, "Should be 20763"


def test_get_skills():
    """
    Test get_skills function
    """
    user=User('naxalov')
    assert type(user.get_skills())==list, "Should be []"
def test_get_completed_by_date():
    user=User('naxalov')
    date=datetime.date(2024,7,30)
    assert type(user.get_completed_by_date((30,7,2024)))==int, "Should be number "
def test_get_weekly():
    user=User('naxalov')
    assert type(user.get_weekly())==int, "Should be number "
def test_get_monthly():
    user=User('naxalov')
    assert type(user.get_monthly())==int, "Should be number"





