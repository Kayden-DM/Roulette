## Roulette
A command-line roulette game written in Python. It uses the random module to spin a number between 0 and 36, and lets the player bet on colours or numbers with a starting balance of 100.

## Features
Colour Betting — Bet on red (even), black (odd), or green (0), with a 1.5x payout for red/black and 5x for green.

Number Betting — Bet on a number between 0 and 36, with a 5x payout for an exact hit and a 2.5x payout for being within range.

Bet Validation — Rejects bets that are non-numeric, non-positive, or larger than the current balance.

Balance Tracking — Deducts each bet before the spin and adds winnings back to the player's money.

Game Over — Ends the game automatically when the player runs out of money.

Continue or Leave — Prompts the player to keep playing or exit after each loss.

Input Validation — Re-prompts on invalid modes, colours, numbers, and menu choices using try/except ValueError.

## Technologies Used
text
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `random` | Spins a number between 0 and 36 |
| Lists (`red`, `black`, `green`) | Define the roulette colour groups |
| `input()` / `print()` | Console interaction |
| `float()` / `int()` | Parses bets and number guesses |
| `try / except` | Handles invalid numeric input |
| `while True` loops | Keeps the game and prompts running |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Save the code as roulette.py.

Open a terminal in the folder containing the file.

Run python roulette.py.

Choose c for colours or n for numbers, enter a bet amount, then make your guess and follow the prompts to continue or leave.

## Improvements
Fix the near-miss range — range(number - 5, number + 6) gives an 11-number window, not the "within 3" stated in the rules; use range(number - 3, number + 4) to match the instructions.

Fix the payout logic — the bet is deducted before the spin and winnings are added as a multiplier of the bet only, so a win can return less than the stake; either add the stake back on a win or don't deduct it up front.
