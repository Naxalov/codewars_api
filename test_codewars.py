from codewars import User


def test_check_username():
    user = User('Naxalov')
    assert user.check_username() == False,' Username does not exist'
    user = User('naxalov')== True,'Correct username'

def test_get_total():
    user = User('naxalov')
    assert user.get_total() == 426, 'Should be 426'

# Test for check_username
