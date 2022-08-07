#Name: Brendan Gee
#Date: 5/3/2021
#Video Link: https://youtu.be/uei4nWWZsJM
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

import Dice_Cups
import random

#main function
def Cups_Dice():
    '''Executes a Cups & Dice game with the user'''

    name = greetUser()
    balance = 100

    #Ask user if they want to play
    while playGame():

        #Generate goal number, print out for user to see
        goal = random.randint(1,100)
        print(f'The number to roll for is {goal}')

        #subtract user Bet from bal
        bet = userBet(balance)
        balance -= bet

        #ask user for number of dice
        diceLst = diceCount()

        #roll the dice in a cup using Cup object
        res = Dice_Cups.Cup(diceLst[0],diceLst[1],diceLst[2])
        print(f'You rolled a sum of {res.roll()}!')

        #game logic to determine if user wins their money back
        award = gameLogic(goal,res,bet)
        balance += award

        #print summary of the game
        printSummary(balance,goal,res,name,award)

        #when balance falls to zero, user can't place anymore bets
        if balZero(balance):
            break

def greetUser():
    '''greets user and asks for their name'''

    print('Hello Player. Welcome to the game of Cups & Dice!')
    return input('Please enter your name: ')

def playGame():
    '''Asks user if they want to play Cups & Dice game.
    returns True if so, False otherwise'''

    while True: #checks user puts correct response
        res = input('Would you like to play Cups & Dice? (Y/N): ')

        if res.upper() == 'Y':
            return True
        elif res.upper() == 'N':
            return False
        else:
            print('Please enter a "Y" or "N"') #if wrong entry, asks again

def userBet(balance):
    '''Asks user for bet. Makes sure it is within range
    of their balance, and not negative'''

    #print out current balance
    print(f'Your current balance is: {balance}')

    while True: #checking for positive integer and not greater than balance
        try:
            res = int(input('Please enter an amount you want to bet. Cannot exceed your balance: '))
        except ValueError: #input string vs int
            print('Please enter a number.')
            continue #restart while loop
        if res > balance: #can't bet more than you have
            print('Please enter an amount less than your balance.')
            continue
        elif res <= 0: #can't bet 0 or negative numbers
            print('Please enter a positive integer amount.')
            continue
        else: #once it checks each condition,
            return res

def diceCount():
    '''Asks user for number of dice they
    want to use for the game'''
    
    reslst = []
    diceType = [6,10,20]

    for i in range(len(diceType)): #iterates through each type of die
        
        while True: #check for negative number inputs, as well as strings
            try:
                res = int(input(f'Enter # of {diceType[i]}-sided dice you wish to use: '))

            except ValueError: #input string vs int
                print('Please enter positive integer values only!')
                continue #restart while loop

            if res < 0: #can't use a negative dice number
                print('Please enter positive integer values only!')
                continue
            else: #if conditions are met, append reslst
                reslst.append(res)
                break #break out of while loop, go to next value of for loop
    return reslst

def gameLogic(goal,res,bet):
    '''Determines how much is added to the user's balance,
    if any'''

    award = 0 #initialize awarded balance at 0

    #when user guesses correctly, award by 10 times user gamble
    if res.getSum() == goal: 
        award += bet*10

    #when user guesses within 3 and lower, award by 5 times user gamble
    elif res.getSum() < goal and res.getSum() + 3 >= goal:
        award += bet*5

    #when user guesses within 10 and lower, award by 2 times user gamble
    elif res.getSum() < goal and res.getSum() + 10 >= goal:
        award += bet*2

    return award

def printSummary(balance,goal,res,name,award):
    '''prints out a summary of the results of the game'''

    print(f'Good game {name}!')
    print('Here are the results of the game:')
    print()
    print(f'You rolled a sum of {res.getSum()} while the number to roll was {goal}')
    print(f'Therefore, you are awarded {award} to your balance')
    print(f'Your new balance total is {balance}')
    print()

def balZero(balance):
    '''Checks if the users balance is zero.
    if it is, user can no longer place any
    bets, and game ends'''

    if balance == 0: #if users balance is zero, ends the game
        print('Your balance has fallen to zero, meaning you cannot place anymore bets.')
        print('Game Over!!')
        return True
    return False #otherwise, asks if they want to continue
