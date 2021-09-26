'''
Some basic sanity tests for purposes of tute preparation
Don't assume these are a thorough suite of tests
'''
from partB import set_name

def test_simple():
    assert set_name("firstname", None, "lastname") == True
    assert set_name("firstname", "middle", "lastname") == True
    assert set_name("f", None, "lastname") == False

def test_firstname():
    assert set_name("a", None, "lastname") == False
    assert set_name("ab", None, "lastname") == False
    assert set_name("abc", None, "lastname") == True
    assert set_name("abcd", None, "lastname") == True
    assert set_name("a" * 29, None, "lastname") == True
    assert set_name("a" * 30, None, "lastname") == True
    assert set_name("a" * 31, None, "lastname") == False

def test_lastname():
    assert set_name("a", None, "lastname") == False
    assert set_name("ab", None, "lastname") == False
    assert set_name("abc", None, "lastname") == True
    assert set_name("abcd", None, "lastname") == True
    assert set_name("firstname", None, "a" * 49) == True
    assert set_name("firstname", None, "a" * 50) == True
    assert set_name("firstname", None, "a" * 51) == False

def test_firstname_chars():
    assert set_name("UPPER", None, "lastname") == True
    assert set_name("lower", None, "lastname") == True
    assert set_name("mIxEd", None, "lastname") == True
    assert set_name("numbers2", None, "lastname") == False
    assert set_name("dash-test", None, "lastname") == True
    assert set_name("DASH-TEST", None, "lastname") == True
    assert set_name("Dash-Test", None, "lastname") == True
    assert set_name("ab-", None, "lastname") == True
    assert set_name("-ab", None, "lastname") == True

def test_lastname_chars():
    pass

def test_middlename():
    pass

def test_middlename_special():
    pass
