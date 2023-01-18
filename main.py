#Rock Paper Scissors By Adi

import json
import random


#Get the Users Choice
def getUserChoice():
    options = ["rock", "paper", "scissors"]
    userInput = input("Enter your choice (rock, paper, scissors) or press 'e' to exit the game: ").lower()
    while userInput not in options and userInput != 'e':
        print("Invalid choice. Please enter rock, paper, scissors or press 'e' to exit the game.")
        userInput = input("Enter your choice (rock, paper, scissors) or press 'e' to exit the game: ").lower()
    return userInput

#Get the computers choice
def getComputerChoice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

#Determine who wins
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

#Play the Game
def playGame():
    
    #Streak of the Current Game
    winStreak = 0
    
        #Get the HighScore
        file = open("highscore.json", "r")
        dataStr = file.read()
        file.close()
        highscore = json.loads(dataStr)["highscore"]
        
    #The game loop
    while True:
        #Get the User's Input
        userInput = getUserChoice()
        
        #If the user Exits
        if userInput == "e":
            break
         
        #Get and display the Computer's choice
        computerChoice = getComputerChoice()
        print("Computer chose:", computerChoice)
        
        #Get the Result of the Game
        gameResult = getRoundResult(userInput, computerChoice)

        if gameResult == "tie":
            print("It's a tie!")
        elif gameResult == "win":
            print("You win!")
            winStreak += 1
        else:
            if winStreak == 0:
                print("You lose")
            else:
                print("You lost with a streak of", winStreak)
            winStreak = 0
        
        #Check if HighScore
        if winStreak > highscore:
            highscore = winStreak
            print("New high score! Your win streak is", winStreak)
            
            #Write to JSON
            with open("highscore.json", "w") as f:
                json.dump({"highscore": highscore}, f)
                
    #Exit the Game
    print("Exiting Game")

    #Run the Game
playGame()
