# Avoid multiple returns
# https://docs.python.org/3/library/stdtypes.html

def set_name(firstName, middleName, lastName):
    flag = True

    if (len(firstName) < 3 or len(firstName) > 30):
        flag = False
    if (len(lastName) < 3 or len(lastName) > 50):
        flag = False

    # opposite of (letters or dashes)
    if not (firstName.isalpha() or "-" in firstName):
        flag = False

    # opposite of (letters or dashes or spaces)
    if (not (lastName.isalpha() or "-" in lastName or \
        "-" in lastName)):
        flag = False
    
    if (middleName != None and len(middleName) > 50):
        flag = False

    if (middleName != None and \
        (len(middleName) > len(firstName) or \
        len(middleName) > len(lastName))):
        flag = False

    # print(flag)
    return flag

# if __name__ == '__main__':
#     set_name("name-", None, "name")
#     set_name("asl", None, "name")
#     set_name("asl-", None, "name")
