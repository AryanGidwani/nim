# Aryan Gidwani
# November 26, 2021
# ICS3UO - A
# This program allows the user to play the game of Nim! Nim is a game where
# there are a certain amount of stones or objects, and each player takes
# turns taking either 1, 2, or 3 stones from the pile. The person who takes
# the last stone from the pile is the loser!

# Test comment

import random
# imports a module that helps with generating random numbers
import sys
# imports a module to help different aspects of the program

def stopProgram(userInput):
    if userInput == "quit":
        sys.exit("Thank you for using this program!")
        # terminates the program
    else:
        pass
        # pass is used to do nothing

winner = "user"
# creates a variable named winner that stores the winner of the game
def computerGame(totalStones):
    global winner
    # makes the winner variable global and accessible
    while True:
        if(totalStones <= 1):
            if winner == "user":
                print("You have beat the computer :)!")
                # tells the user that they have lost
                return
                # effectively exits the function
                totalStones = random.randint(15, 31)
                # finds a new, random number for the number of stones
            else:
                print("You have lost to the computer! :(")
                # tells the user that they have beat the computer
                return
                # effectively exits the function
                totalStones = random.randint(15, 31)
                # finds a new, random number for the number of stones

        print("There are " + str(totalStones) + " total stones in the pile! Begin by choosing how many stones you " + "\n" + " would like to remove!")
        # informs the user the number of stones there are in the pile
        computerStones = random.randint(1, min(totalStones, 3))
        # computer chooses the number of stones they want to remove
        removedStones = input("Would you like to remove 1, 2, or 3 stones? Please input the number only, not in words. All decimals will be rounded. ")
        # asks the user for the number of stones they want removed
        stopProgram(removedStones)
        # calls the quit function to see if the user inputted "quit"
        removedStones = int(removedStones)
        # casts it to an integer and rounds any decimals
        if (removedStones == 1) or (removedStones == 2) or (removedStones == 3):
            if (int(removedStones) < totalStones):
                totalStones = totalStones - removedStones
                # removes the amount of stones
                winner = "user"
                # sets the winner to the user
                if computerStones < totalStones:
                    winner = "computer"
                    # sets the winner to the computer
                    totalStones = totalStones - computerStones
                    # subtracts the amount that the computer wants to remove
                    print("The computer has removed " + str(computerStones) + " total stones!")
                    # tells the user the number of stones the computer has removed

                elif totalStones == 3:
                    winner = "computer"
                    # sets the winner to the computer
                    computerStones = random.randint(1, 2)
                    # chooses a random number from 1 to 2 if there are only
                    # 3 stones in the pile
                    totalStones = totalStones - computerStones
                    # updates variable
                    print("The computer has removed " + str(computerStones) + " total stones!")
                    # tells the user the number of stones the computer has removed

                elif totalStones == 2:
                    winner = "computer"
                    # sets the winner to the computer
                    computerStones = 1
                    # sets computerStones to 1 if the pile has 2 stones
                    totalStones = totalStones - computerStones
                    # updates variable
                    print("The computer has removed " + str(computerStones) + " total stones!")
                    # tells the user the number of stones the computer has removed
                    
            elif (int(removedStones) == totalStones):
                totalStones = totalStones - removedStones
                # removes the amount of stones if the user decides to get rid
                # of the entire pile
                winner = "computer"
                # sets the winner to the computer
  
            else :
                print("You have inputted an invalid input!")
                # invalid input message
                
        else :
            print("You have inputted an invalid input!")
            # invalid input message
            
playerOneTurn = True
# boolean value which determines whether it is player one's turn
def playerGame(totalStones):
    global playerOneTurn
    # makes the variable global
    while True:
        print("There are " + str(totalStones) + " total stones in the pile!")
        # informs the user the number of stones in the pile
        if (totalStones <= 0):
            if playerOneTurn:
                print("Player 2, you have lost to player 1!")
                # tells the users that player 1 has lost to player 2
                return
                # effectively exits the function

            else :
                print("Player 1, you have lost to player 2!")
                # tells the users that player 2 has lost to player 1
                return
                # effectively exits the function

        while True:
            if playerOneTurn:
                playerInput = input("Player 1: Would you like to remove 1, 2, or 3 stones? Input the number only, not in words. All numbers with decimals will be rounded.")
                # asks player 1 how many stones they would like to remove
                stopProgram(playerOneTurn)
                # checks to see if the player wanted to quit

            else:
                playerInput = input("Player 2: Would you like to remove 1, 2, or 3 stones? Input the number only, not in words. All numbers with decimals will be rounded.")
                # asks player two how many stones they would like to remove
                stopProgram(playerInput)
                # checks to see if they wanted to quit
            playerInput = int(playerInput)
            # casts it to an integer
            if ((playerInput >= 1) and (playerInput <= 3)):
                if (int(playerInput) < totalStones):
                    totalStones = totalStones - playerInput
                    # subtracts the amount that player one wants to remove
                    break
                    # breaks the loop process
                
                elif (int(playerInput) == totalStones):
                    totalStones = totalStones - playerInput
                    # subtracts the amount that player one wants to remove
                    break
                    # breaks the loop process
                
                else :
                    print("You have inputted an invalid input!")
                    # invalid input message
            else :
                print("One of you players have entered in an invalid value! Remember, the values must be either 1, 2, or 3!")
                # invalid input message
                
        playerOneTurn = not playerOneTurn
        # changes the boolean value at the end
        
def modeChooser():
    while True:
        stones = random.randint(15, 30)
        # generates the number of stones in the pile
        print("a: Player vs Computer" + "\n" + "b: Player vs Player")
        # shows the different options that the user can play
        chosenMode = input("Enter in the letter corresponding to the mode that you want to play! Enter: ")
        # asks the user for the mode that they want to play
        stopProgram(chosenMode)
        # calls the quit function to see if the user inputted "quit"
        if chosenMode == "a":
            computerGame(stones)
            # calls the computerGame function

        elif chosenMode == "b":
            playerGame(stones)
            # calls the playerGame function

        else:
            print("You have inputted an invalid input! Please enter one of the letters!")
            # invalid input message
            
name = input("Hello! What is your name? ")
# asks the user for their name
stopProgram(name)
# checks to see if the user typed in quit
print("Hello " + name + "! This is the game of Nim! As seen below, there are a certain number of stones in a pile. Each player will take turns only taking either 1, 2, or 3 " + "\n" + " stones from the pile. This process will continue until the player who is forced" + "\n" + "to take the last stone; this player is the loser of the game! Good luck and have fun!")
# introductory message

modeChooser()
# calls the modeChooser function
