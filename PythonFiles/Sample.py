import os
import random,sys
from tkinter import *


# Game 1 - War
def game1():
    bank = 100

    while bank > 0:
        print("Bank balance is:", bank)
        bet = input("How much is your bet? Press 'e' to exit: ")

        if bet == 'e':
            break

        if bet.isdigit() == True:
            bet = int(bet)

        # Computer picks a random number between 1 and 10
        House = random.randrange(0, 11)
        print("The computer draws:", House)

        # Player gets a random number between 1 and 10
        input("Press ENTER to draw!" + os.linesep)
        Player = random.randrange(0, 11)
        print("You draw:", Player)

        if Player > House:
            print("You win!" + os.linesep)
            bank += bet
            print(f"New balance: {bank}." + os.linesep)

        elif Player < House:
            print("You lost." + os.linesep)
            bank -= bet
            print("New balance:", bank + os.linesep)

        else:
            print("It's a tie! War begins." + os.linesep)

            for _ in range(3):
                # Computer picks a random number between 1 and 10
                House = random.randrange(1, 10)
                print("The computer draws:", House + os.linesep)

                # Player gets a random number between 1 and 10
                input("Press ENTER to draw!" + os.linesep)
                Player = random.randrange(0, 11)
                print("You draw:", Player + os.linesep)

                if Player > House:
                    print("You win the war!" + os.linesep)
                    bank += bet
                    print(f"New balance: {bank}." + os.linesep)
                    break

                elif Player < House:
                    print("You lost the war." + os.linesep)
                    bank -= bet
                    print("New balance:", bank + os.linesep)
                    break

            else:
                print("It's another tie! War continues." + os.linesep)

    print("Thank you for playing." + os.linesep)

# Game 2 - Blackjack
def game2():
    bank = 100

    while bank > 0:
        print("Bank balance is:", bank)
        bet = input("How much is your bet? Press 'e' to exit: ")

        if bet == 'e':
            break

        if bet.isdigit() == True:
            bet = int(bet)

        # Computer and player get two initial cards
        computer_cards = [random.randint(1, 10) for _ in range(2)]
        player_cards = [random.randint(1, 10) for _ in range(2)]
        
        print("Computer's cards:", computer_cards)
        print("Your cards:", player_cards)

        # Game loop for player's actions
        while True:
            action = input("Do you want to hit or stand? ").lower()

            if action == 'hit':
                # Player receives another card
                player_cards.append(random.randint(1, 10))
                print("Your cards:", player_cards)
            elif action == 'stand':
                break
            else:
                print("Invalid input! Please enter 'hit' or 'stand'.")

        # Computer's turn
        while sum(computer_cards) < 17:
            computer_cards.append(random.randint(1, 10))

        print("Computer's final cards:", computer_cards)

        # Determine the winner
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)

        if player_score > 21:
            print("Bust! You lose.")
            bank -= bet
        elif computer_score > 21 or player_score > computer_score:
            print("You win!")
            bank += bet
        elif player_score < computer_score:
            print("You lose.")
            bank -= bet
        else:
            print("It's a tie.")

        print("New balance:", bank)
        print(os.linesep)  # Add a new line between iterations

    print("Thank you for playing.")


# Quit
def quit():
    print("Bye!")
    sys.exit()


# Tkinter Window
win = Tk()
win.title("CASINO GAMES")
win.geometry("400x300")

title_font = ('Arial', 24, 'bold')
button_font = ('Arial', 16)

title_label = Label(win, text="CASINO GAMES", font=title_font)
title_label.pack(pady=20)

war_button = Button(win, text="War", font=button_font, command=game1)
war_button.pack(pady=10)

blackjack_button = Button(win, text="Blackjack", font=button_font, command=game2)
blackjack_button.pack(pady=10)

quit_button = Button(win, text="Quit", font=button_font, command=win.quit)
quit_button.pack(pady=10)

win.mainloop()