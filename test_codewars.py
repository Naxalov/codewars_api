import pytest
from codewars import User

user = User("Kamoliddin-Otamurodov")

def get_total_test():
    assert user.get_total() == 272 , "Should be 272"

def check_user_test():
    assert user.check_user() == True , "Should be True"

def get_id_test():
    assert user.get_id() == "6543194c386565f86f4d7c7c" , "Should be 6543194c386565f86f4d7c7c"

def get_username_test():
    assert user.get_username() == "Kamoliddin-Otamurodov" , "Should be Kamoliddin-Otamurodov"

def get_name_test():
    assert user.get_name() == None , "Should be None"

def get_honor_test():
    assert user.get_honor() == 776 , "Should be 776"

def get_clan_test():
    assert user.get_clan() == None , "Should be None"

def get_leadpos_test():
    assert user.get_leadpos() ==  52623, "Should be 52623"

check_user_test()
get_id_test()
get_username_test()
get_name_test()
get_honor_test()
get_clan_test()
get_leadpos_test()
get_total_test()