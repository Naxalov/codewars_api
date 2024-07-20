from codewars import User

def test_get_total():
    user = User('Naxalov')
    assert user.get_total() == 426, 'Should be 426'