def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    contains_number = False
    contains_lower = False
    contains_upper = False
    
    for char in password:
        contains_number = char.isnumeric()
        if char.islower():
            contains_lower = True
        if char.isupper():
            contains_upper = True
            
    if password in ['password', 'iloveyou', '123456']:
        return 'Horrible password'   
    elif len(password) >= 12 and contains_number and contains_lower and contains_upper:
        return 'Strong password'
    elif len(password) >= 8 and contains_number:
        return 'Moderate password'
    else:
        return 'Poor password'
