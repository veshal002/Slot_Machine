My first program I am using to learn Python and Git.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Slot Machine Game 🎰 :

This project is a simple Slot Machine Game coded in Python, designed to simulate a slot machine experience. The game allows users to deposit a balance, place bets on multiple lines, and spin to win based on randomly generated symbols.

Features -
Deposit Balance: Start by depositing a balance to play.
Customizable Betting Lines and Amount: Choose the number of lines to bet on (up to 3) and set the amount per line.
Randomized Slot Symbols: Each spin generates a new set of symbols based on predefined symbol odds.
Winnings Calculation: Winning lines and amounts are automatically calculated and displayed after each spin.
Gameplay Instructions
Deposit an amount to your balance.
Choose the number of lines to bet on, from 1 to 3.
Set your bet amount for each line (between 10 and 100).
Spin the slot machine and check if you've won!
Quit anytime by pressing q to end the game with your remaining balance.
Code Overview
Main Components
Symbol Counts and Values: Predefined values determine the frequency and payout for each symbol.

symbol_count: Dictates the occurrence of each symbol on the slot machine.
symbol_value: Defines the payout multiplier for each symbol.
Game Functions:

deposit(): Prompts the user to deposit an amount to play.
get_number_of_lines(): Lets the user select the number of lines to bet on.
get_bet(): Gets the betting amount for each line.
get_slot_machine_spin(): Generates a randomized slot outcome for each column.
check_winnings(): Calculates the winnings based on matched symbols in the spin.
print_slot_machine(): Displays the slot machine's spin result in a visual format.
Main Game Loop:

The main() function starts the game loop, handles user input, and updates the balance.

Requirements
No external libraries are needed. Just ensure you have Python installed on your system.
