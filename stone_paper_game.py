import random

choice = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

print("-----ROCK PAPER SCISSOR GAME-----")

while True:
    user = input("\nEnter rock, paper or scissor (L to leave): ").lower()

    if user == "l":
        break

    if user not in choice:
        print("----Invalid Input Try Again----")
        continue

    computer = random.choice(choice)

    print("Computer chose:", computer)

    if user == computer:
        print("It is tie!")
    elif user == "rock":
        if computer == "scissor":
            print("You win")
            user_score = user_score + 1
        else:
            print("Computer win")
            computer_score = computer_score + 1
    elif user == "paper":
        if computer == "rock":
            print("You win")
            user_score = user_score + 1
        else:
            print("Computer win")
            computer_score = computer_score + 1
    elif user == "scissor":
        if computer == "paper":
            print("You win")
            user_score = user_score + 1
        else:
            print("Computer win")
            computer_score = computer_score + 1

    print("User_score",user_score)
    print("Computer_score",computer_score)

print("\n-----THANKYOU FOR PLAYING-----")
print("Final Score -> You:", user_score, "| Computer:", computer_score)
    
