import random

def rps(your_move):
    computer_move = random.randint(1, 3)
    if computer_move == 1:
        if your_move == 2:
            print("Computer plays Roc. You play Panther. You win!")
        elif your_move == 3:
            print("Computer plays Roc. You play Stingray. You lose!")
        else:
            print("Computer plays Roc. You play Roc. Tie game!")
    elif computer_move == 2:
        if your_move == 2:
            print("Computer plays Panther. You play Panther. Tie game!")
        elif your_move == 3:
            print("Computer plays Panther. You play Stingray. You win!")
        else:
            print("Computer plays Panther. You play Roc. You lose!")
    elif computer_move == 3:
        if your_move == 2:
            print("Computer plays Stingray. You play Panther. You lose!")
        elif your_move == 3:
            print("Computer plays Stingray. You play Stingray. Tie game!")
        else:
            print("Computer plays Stingray. You play Roc. You win!")

def main():
    print("Welcome to Roc, Panther, Stingray!")
    move = int(input("Type 1 for Roc, 2 for Panther, and 3 for Stingray: "))
    rps(move)

main()