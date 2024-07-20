import pytest
from codewars import User



def get_total_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_total() == 272 , "Should be 272"

def check_user_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.check_user() == True , "Should be True"
    user = User("Kamoliddin-Otamurodo")
    assert user.check_user() == False, "Username does not exist"

def get_id_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_id() == "6543194c386565f86f4d7c7c" , "Should be 6543194c386565f86f4d7c7c"

def get_username_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_username() == "Kamoliddin-Otamurodov" , "Should be Kamoliddin-Otamurodov"

def get_name_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_name() == "Kamoliddin" , "Should be Kamoliddin"

def get_honor_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_honor() == 776 , "Should be 776"

def get_clan_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_clan() == "" , "Should be None"

def get_leadpos_test():
    user = User("Kamoliddin-Otamurodov")
    assert user.get_leadpos() ==  52623, "Should be 52623"

check_user_test()
get_id_test()
get_username_test()
get_name_test()
get_honor_test()
get_clan_test()
get_leadpos_test()
get_total_test()