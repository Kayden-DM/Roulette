import random


money = 100
green= [0]
red = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
black = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]


print("welcome to roulette. You have 100 money. You can place bets on colours or numbers. If you run out of money, the game ends.")
print("Every correct guess of a number or green gives you 5x your bet. \nEvery guess within 3 of the number gives you 2.5x your bet. \nEvery guess of correct colour gives you 1.5x your bet.")


def mode():
    gmode = input("Choose a mode between colours (c) and numbers (n): ").lower().strip()
    return gmode


while True:
    
    if money == 0:
        print("You have no money left.")
        exit()

    gmode = mode()
    if gmode == "c":
        print("You have chosen colours")
        random_number: int = random.randint(0, 36)
        print("You have", money, "dollars.")

        while True:
            try:
                bet = float(input("Choose a bet amount: "))
            except ValueError:
                print("You must enter a number.")
                continue
            if bet > money:
                print("You don't have enough money.")
                continue
            elif bet <= 0:
                print("You must bet a positive amount.")
                continue
            break

        money -= bet
        print(f"You have bet {bet} dollars.")

        while True:
            colour = input("Choose a colour between red (even), black (odd) and green (0): ").lower().strip()
            if colour in ["red", "black", "green"]:
                break
            print("Choose between one of the options")

        if colour == "red" and random_number in red:
            money += bet * 1.5
            print(f"You won {bet * 1.5} dollars.")
            print("The number was ", random_number)
            continue

        elif colour == "black" and random_number in black:
            money += bet * 1.5
            print(f"You won {bet * 1.5} dollars.")
            print("The number was ", random_number)
            continue

        elif colour == "green" and random_number in green:
            money += bet * 5
            print(f"You won {bet * 5} dollars.")
            print("The number was ", random_number)
            continue

        else:
            print(f"You lost. The number was {random_number}.")
            while True:
                quit = input("Would you like to continue (c) or leave (l)? ").lower().strip()
                if quit == "l":
                    print("Thanks for playing")
                    exit()
                elif quit == "c":
                    break
                print("Invalid option, try again: ")


    elif gmode == "n":
        print("You have chosen numbers")

        random_number: int = random.randint(0, 36)
        print("You have", money, "dollars.")

        while True:
            try:
                bet = float(input("Choose a bet amount: "))
            except ValueError:
                print("You must enter a number.")
                continue
            if bet > money:
                print("You don't have enough money.")
                continue
            elif bet <= 0:
                print("You must bet a positive amount.")
                continue
            break

        money -= bet
        print(f"You have bet {bet} dollars.")

        while True:
            try:
                number = int(input("Choose a number between 0 and 36: "))
            except ValueError:
                print("You must enter a number.")
                continue
            if number < 0 or number > 36:
                print("Invalid number. Try again: ")
                continue
            break

        if number == random_number:
            money += bet * 5
            print(f"You have won {bet * 5} dollars.")
            print("The number was ", random_number)
            continue

        elif random_number in range(number - 5, number + 6):
            money += bet * 2.5
            print(f"Close enough. You have won {bet * 2.5} dollars.")
            print("The number was ", random_number)
            continue

        else:
            print(f"You lost. The number was {random_number}.")
            while True:
                quit = input("Would you like to continue (c) or leave (l)? ").lower().strip()
                if quit == "l":
                    print("Thanks for playing")
                    exit()
                elif quit == "c":
                    break
                print("Invalid option, try again: ")
    else:
        print("Invalid choice.")