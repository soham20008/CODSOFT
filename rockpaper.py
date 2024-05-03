import random

def rock_paper_scissors():
    print(f"1. Rock\n2. paper.\n3. Scissores")
    n = int(input("Type chose your number "))
    l = ["Rock","Paper","Scissores"]
    com = random.choice(l)
    print("Computer choice is ",com)
    if n == 1 and com == "Rock":
        print("It's Tie")
    elif n == 1 and com == "Paper":
        print("Computer win")
    elif n == 1 and com == "Scissores":
        print("you win")

    elif n == 2 and com == "Rock":
        print("You win")

    elif n == 2 and com == "Paper":
        print("it's a tie")
    elif n == 2 and com == "Scissores":
        print("computer win")

    elif n == 3 and com == "Rock":
        print("computer win")

    elif n == 3 and com == "Paper":
        print("you win")

    elif n == 3 and com == "Scissores":
        print("it's a tie")

    la  = str(input("Type Yes if you want to play again or No if you want to exit. "))
    if la =="yes":
       rock_paper_scissors()
    elif la == "no":
        feedback = str(input("type your feedback here about this game. "))
        print(f"Thank you for your valuable feedback.\tWe apreciate your afforts.")
        exit()

print(f"Please read carefully instruction given below.\n1. These game is fun purpose only please don't take it seriously.\n2. How winnner will decide.\n * Rock beats the scissors.\n * scissors beats the paper.\n * Paper beats the rock. \n * If two of them choose the same then its a tie.\n3. Thank you for reading the instruction. Enjoy your game.\n")

rock_paper_scissors()

