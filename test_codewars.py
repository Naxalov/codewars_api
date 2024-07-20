from codewars import User

def test_check_username():
    user = User('Naxalov')
    assert user.check_username() == False,' Username does not exist'
    user = User('naxalov')== True,'Correct username'

def test_get_total():
    user = User('naxalov')
    assert user.get_total() == 426, 'Should be 426'

def test_get_name():
    """
    Test get_name function
    """

def test_get_honor():
    """
    Test get_honor function
    """
def test_get_clan():
    """
    Test get_clan function
    """
def test_get_leaderboard_position():
    """
    Test get_leaderboard_position function
    """
def test_get_skills():
    """
    Test get_skills function
    """





