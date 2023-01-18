import json
import random

def getUserChoice():
    options = ["rock", "paper", "scissors"]
    userInput = input("Enter your choice (rock, paper, scissors) or press 'e' to exit the game: ").lower()
    while userInput not in options and userInput != 'e':
        print("Invalid choice. Please enter rock, paper, scissors or press 'e' to exit the game.")
        userInput = input("Enter your choice (rock, paper, scissors) or press 'e' to exit the game: ").lower()
    return userInput

def getComputerChoice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def getRoundResult(userInput, computerChoice):
    if userInput == computerChoice:
        return "tie"
    elif userInput == "rock" and computerChoice == "scissors":
        return "win"
    elif userInput == "paper" and computerChoice == "rock":
        return "win"
    elif userInput == "scissors" and computerChoice == "paper":
        return "win"
    else:
        return "lose"

def playGame():
    winStreak = 0
    try:
        file = open("highscore.json", "r")
        dataStr = file.read()
        file.close()
        highscore = json.loads(dataStr)["highscore"]
    except:
        highscore = 0
        
    while True:
        userInput = getUserChoice()
        if userInput == "e":
            break
        computerChoice = getComputerChoice()
        print("Computer chose:", computerChoice)
        roundResult = getRoundResult(userInput, computerChoice)

        if roundResult == "tie":
            print("It's a tie!")
        elif roundResult == "win":
            print("You win!")
            winStreak += 1
        else:
            if winStreak == 0:
                print("You lose")
            else:
                print("You lost with a streak of", winStreak)
            winStreak = 0

        if winStreak > highscore:
            highscore = winStreak
            print("New high score! Your win streak is", winStreak)
            with open("highscore.json", "w") as f:
                json.dump({"highscore": highscore}, f)
    print("Exiting Game")

playGame()