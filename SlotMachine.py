# SLOT - MACHINE 

import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():# .items returns all the keys and values and assoicated with the dictionaries above
        for _ in range (symbol_count): # _ is an anonymous variable present in python when used in loop so we can have an unused variable.
            all_symbols.append(symbol)# append adds a single item to end of the existing list.

    columns = [] # nested lists - stores columns and not rows.  
    for _ in range(cols): # _ - anonymous way in python to use so there will be a unused variable
        column= []
        current_symbols = all_symbols[:] # : - its a slice operator and it will copy a list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns): # enumerate give index as loop through and as well as item.
            if i !=len(columns) - 1:
                print(column[row], end =" | ") # | - pipe operator it connects the output from one method with the output from another method.
            else:
                print(column[row], end = " ") # end = is also called a \n - new line thing
        print()

        
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


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print(f"You do not have enough balance to bet that amount, your current balance is : rs{balance}")
        else:
            break

    print(f"You are betting rs{bet} on {lines} lines. Total bet is equal to {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines ,bet, symbol_value)
    print(f"You won Rs {winnings}.")
    print(f"You won on lines : ", *winning_lines) # 
    balance += winnings - total_bet
    return balance

def main():
    balance = deposit()
    while True :
        print(f"current balance is rs{balance}")
        answer = input ("press enter to play (q to quit).")
        if answer == "q":
            break
        balance = spin(balance)
    print(f"you are left with balance = Rs {balance}")

main()