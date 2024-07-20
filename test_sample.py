import pytest
from codewars import User
user = User('allamurodxakimov')

def chekc_username():
    assert user.check_username() == False, 'Username error'
    user = User('allamurodxakimov') == True , 'Connect username'
