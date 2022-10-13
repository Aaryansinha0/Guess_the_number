import random
from art import logo
from replit import clear

EASY_LEVEL = 10
HARD_LEVEL = 5
BOSS_LEVEL = 1


def check_answer(guess, answer, turns):
    if guess > answer:
        print("No! you guessed too high")
        return turns - 1
    elif guess < answer:
        print("You guessed too low!")
        return turns - 1
    else:
        print(f"You guessed it right... YOU WON! your answer is {answer}")
        if input("Do you want to play again? 'y' or 'n' \n").lower() == "y":
            clear()
            game()
        else:
            print("Have a great Time!")


def difficulty():
    level = input("choose a level.. 'easy' or 'hard' or 'boss' \n").lower()
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL
    else:
        return BOSS_LEVEL


def game():

    print(logo)
    print("Welcome to my Game!")
    name = input("What is your name? \n").title()
    print(f"Hey {name}, I am guessing a number try if you can guess it!")
    answer = random.randint(1, 100)
    turns = difficulty()
    guess = 0

    while turns != 0:
        print(f"You have {turns} turns left. Guess the number wisely")
        guess = int(input("Guess the number!!! \n"))
        turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You lose! you could not guess the number")
        if input("Do you wanna to play again? 'y' or 'n' \n").lower() == "y":
            clear()
            game()
        else:
            print(f"Have a great Time {name}!")
    elif guess != answer:
        print("Guess again! \n")


game()
