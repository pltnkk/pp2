import random

def guess_game():
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    snums = random.randint(1,20)
    for i in range (1,7):
        print("Take a guess.")
        g = int(input())
        if g == snums:
            print("Good job, " + name + "! You guessed my number in " + str(i) + " guesses!")
        elif g < snums:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    else:
        print("No. The number I was thinking of was " + str(snums))

guess_game()

