import pytest
from codewars import User

def chekc_username():
    user = User('allamurodXakimov')
    assert user.check_username() == False, 'Username error'
    user = User('allamurodxakimov') == True , 'Connect username'
