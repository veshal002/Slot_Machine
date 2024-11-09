# techwithtim video name = Learn python with this ONE project. time = 29:30

import random



MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS= 3

symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machien_spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():# .items returns all the keys and values and assoicated with the dictionaries above
        for _ in range (symbol_count): # _ is an anonymous variable present in python when used in loop so we can have an unused variable.
            all_symbols.append()# append adds a single item to end of the existing list.

    columns = [[], [] , []] # nested lists - stores columns and not rows.  
    for col in range(cols):
        column= []
        current_symbols = all_symbols[:] # : - its a slice operator and it will copy a list
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def deposit():
    while True: # while True is used because this function is used repeatedly so making it TRUE will enable the function automatically.
        amount = input("Enter the deposit value : ")
        if amount.isdigit(): # isdigit is used to check if the value entered is a number rather than a string or something else.
            amount = int(amount) # If the entered value is integer then it is typecasted and stored as integer value from string value.
            if amount > 0:
                break
            else:
                print("Please enter a valid amount.")
        else:
            print("please Enter an amount")

    return amount

def get_number_of_lines():
    while True: 
        lines = input(f"Enter the number lines to bet on (1-{MAX_LINES}) ")
        if lines.isdigit(): 
            lines = int(lines) 
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Please enter a valid lines.")
        else:
            print("please Enter an number")
    return lines

def get_bet():
    while True: 
        amount = input(f"Enter the number for bet on each line : ")
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between rs{MIN_BET} - rs{MAX_BET}.")
        else:
            print("please Enter an number")
    return amount


def main():
    balance= deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print(f"You do not have enough balance to bet that amount, your current balance is : rs{balance}")
        else:
            break
    print(f"You are betting rs{bet} on {lines} lines. Total bet is equal to {total_bet}")

main()