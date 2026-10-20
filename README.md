Roulette Game
A command-line Python roulette game where the player starts with $100 and bets on colours or numbers, with payouts for exact matches, close guesses, or correct colours.

Concepts Used
Random Module — random.randint(0, 36) simulates the roulette wheel spin.

Lists — red and black lists store the valid numbers for each colour to check bets.

While Loops with Validation — nested loops keep re-prompting until the player enters a valid bet, colour, or number.

Features
Two Game Modes — bet on colours (red/black/green) or specific numbers (0–36).

Tiered Payouts — 5x for exact hits, 2.5x for numbers within 5, 1.5x for correct colour.

Balance Tracking — money is deducted on bet and paid out on a win, ending when it hits zero.

Improvements
Deduplicate Code — the colour and number branches repeat the bet/quit logic; extract into shared functions.

Fix Payout Bug — the win message says "within 3" but the code checks ±5, and the "close" check is off (uses a 10-number range, not symmetric around the guess).

Handle Decimal Money — round balances and payouts to 2 decimal places to avoid float drift like 149.99999.
