def check_password(password):
    #get uppers
    uppers = False
    for chars in password:
        if chars.isupper() == True:
            uppers = True
            break
    #get lowers
    lowers = False
    for chars in password:
        if chars.islower() == True:
            lowers = True
            break
    #numeric
    numeric = False
    for chars in password:
        if chars.isnumeric() == True:
            numeric = True
            break
    if (uppers and lowers and numeric and len(password) >= 12):
        return "Strong password"
    elif (numeric and len(password) >= 8):
        return "Moderate password"
    elif (password == "password" or password == "iloveyou" or password == "123456"):
        return "Horrible password"
    else: return "Poor password"
