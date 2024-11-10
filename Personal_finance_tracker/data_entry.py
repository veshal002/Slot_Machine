# used for collecting data from user.
from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False): # allow_default=False - it will help in selecting the current date.
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format - please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)
    
def get_amount():
    try:
        amount = float(input("Enter the amount : Rs "))
        if amount <= 0:
            raise ValueError("amount must be a non - negative non-zero value. ")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense ): ".upper())
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("invalid Category. PLease enter 'I' for income or 'E' for Expense.")
    return get_category()


def get_description():
    return input("Enter a description of your transaction : ")