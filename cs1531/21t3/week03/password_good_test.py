'''
Tests for check_password()
'''
from password_good import check_password

def test_horrible():
    assert check_password("password") == "Horrible password"
    assert check_password("iloveyou") == "Horrible password"
    assert check_password("123456") == "Horrible password"

def test_poor():
    assert check_password("hunter2") == "Poor password"
    assert check_password("abc123") == "Poor password"
    assert check_password("correcthorsebatterystaple") == "Poor password"

def test_moderate():
    assert check_password("CoolDude86") == "Moderate password"
    assert check_password("cooldude86") == "Moderate password"
    assert check_password("awesome1") == "Moderate password"

def test_strong():
    assert check_password("GJ7fJ8dW34y7") == "Strong password"
    assert check_password("MyVerySecurePassword123") == "Strong password"
    assert check_password("*&)%*Q#%Y&Qw#2") == "Strong password"
