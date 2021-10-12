from datetime import datetime

data = []

def date_to_age(date):
    #30/06/2000
    dob = datetime.strptime(date, "%d/%m/%Y")
    diff = datetime.now() - dob
    return diff.days // 365

def add_name_age(name, date):
    new_person = {
        "name": name,
        "age": date_to_age(date)
    }
    data.append(new_person)

def clear_names_ages():
    data.clear()

def get_names_ages(min_age):
    return [ person for person in data if person["age"]>=min_age]

if __name__ == "__main__":
    print(date_to_age("30/06/2000"))
