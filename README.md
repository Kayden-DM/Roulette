This README is made with AI

🎰 Python Roulette Game
A simple command-line roulette game built with Python. Players start with 100 money and can place bets on either colours (red, black, or green) or numbers (0–36). Correct guesses pay out at different multipliers depending on how close the bet was. The game ends when the player runs out of money or chooses to leave. It's a great beginner project for learning about random numbers, loops, conditionals, and user input validation in Python.

📖 Python Roulette Game
The Python Roulette Game is a console-based simulation of roulette. The player begins with 100 money and can choose between two betting modes:

Colours mode (c) – Bet on red, black, or green.

Numbers mode (n) – Bet on a specific number between 0 and 36.

A random number between 0 and 36 is generated for each round. Payouts depend on how accurate the bet was:

Correct number or green → 5× the bet

Within 5 of the number → 2.5× the bet

Correct colour → 1.5× the bet

All bets are validated to ensure the player bets a positive amount they can actually afford. If the player loses, they're asked whether to continue or leave. If their money ever reaches zero, the game automatically ends.

✨ Features
Starting balance of 100 money – Gives the player a fixed bankroll to begin with.

Two game modes – Colours (c) and Numbers (n).

Random number generation – A new number from 0 to 36 each round using random.randint().

Colour betting – Bet on red (even numbers), black (odd numbers), or green (0).

Number betting – Bet on any number between 0 and 36.

Tiered payouts:

Exact number or green → 5× bet

Within 5 of the number → 2.5× bet

Correct colour → 1.5× bet

Bet validation – Rejects non-numeric, negative, zero, or over-budget bets.

Number validation – Ensures the chosen number is between 0 and 36.

Continue or leave prompt – After a loss, the player can choose to keep playing or exit.

Automatic game over – Ends immediately when money reaches zero.

Case-insensitive input – Accepts uppercase or lowercase letters.

🛠️ What It Uses
Language & Library
Python 3

random – Python's built-in module for generating random numbers.

Key Variables
Variable	Purpose
money	The player's current balance (starts at 100).
green	A list containing the number 0.
red	A list of even numbers from 2 to 36.
black	A list of odd numbers from 1 to 35.
gmode	Stores the player's chosen mode (c or n).
random_number	The randomly generated number for the round.
bet	The amount of money the player wagers.
colour / number	The player's chosen bet (colour or number).
Key Functions
Function	Purpose
mode()	Prompts the player to choose between colours (c) and numbers (n).
Python Concepts Demonstrated
The random module – Using random.randint(0, 36).

Lists – Storing valid colour numbers.

while True loops – For the main game loop and input validation.

Conditional logic – Checking for wins, losses, and near-misses.

Exception handling – try/except blocks for safe numeric input.

String methods – .lower() and .strip() for clean input.

range() – Checking whether a number falls within a range.

F-strings – Formatted output for winnings and messages.

exit() – Ends the game cleanly.

Type hints – e.g., random_number: int.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays messages and results.

float() – Converts input into a decimal number (for bets).

int() – Converts input into a whole number (for the chosen number).

random.randint() – Generates a random number between 0 and 36.

exit() – Terminates the program.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
roulette.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as roulette.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python roulette.py
Follow the prompts to place your bets and enjoy the game!

🖥️ Example Session
text
welcome to roulette. You have 100 money. You can place bets on colours or numbers. If you run out of money, the game ends.
Every correct guess of a number or green gives you 5x your bet. 
Every guess within 3 of the number gives you 2.5x your bet. 
Every guess of correct colour gives you 1.5x your bet.
Choose a mode between colours (c) and numbers (n): c
You have chosen colours
You have 100 dollars.
Choose a bet amount: 20
You have bet 20.0 dollars.
Choose a colour between red (even), black (odd) and green (0): red
You won 30.0 dollars.
The number was  14
Choose a mode between colours (c) and numbers (n): n
You have chosen numbers
You have 110.0 dollars.
Choose a bet amount: 50
You have bet 50.0 dollars.
Choose a number between 0 and 36: 17
Close enough. You have won 125.0 dollars.
The number was  19
Choose a mode between colours (c) and numbers (n): 
🐍 Made with Python
This project is written entirely in Python 3 using only the standard library. It's a fun and practical example of how loops, conditionals, and randomization can be combined to build a small game.

Whether you're a beginner practicing control flow or someone who wants a quick roulette simulation, this project is a great starting point.

💡 Possible Future Improvements
Add more bet types – e.g., odd/even, high/low, dozens, or columns.

Save and load money between sessions using a file.

Add a visual wheel or animated spin (with Tkinter or Pygame).

Track statistics – Wins, losses, biggest payout, etc.

Allow custom starting balance.

Add sound effects for wins and losses.

Improve the "close enough" range to match the printed rules (currently 5, not 3).

Split the code into functions for better organization and readability.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.

