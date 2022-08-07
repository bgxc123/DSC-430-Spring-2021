#Name: Brendan Gee
#Date: 5/3/2021
#Video Link: https://youtu.be/FkIHrciTj0Y
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

import random
class SixSidedDie:
    '''class that represents a six sided die'''
    
    #class variables for easy mapping when inheriting from this class
    num = 6
    string = 'Six'

    def roll(self):
        '''rolls one six sided die and returns
        the result'''
        self.d = random.randint(1,self.num) #random int between 1 and num
        return self.d

    def getFaceValue(self):
        '''returns the current face value of the die'''
        return self.d
    
    def __repr__(self):
        '''instance representation'''
        return f'{self.string}SidedDie({self.d})'

class TenSidedDie(SixSidedDie):
    '''class that represents a ten sided die.
    Inherits from the SixSided Die class.'''

    #Just need to update class variables, no need to rewrite methods
    num = 10 #for roll method
    string = 'Ten' #for repr method

class TwentySidedDie(SixSidedDie):
    '''class that represents a twenty sided die
    Inherits from the SixSided Die class.'''

    #Just need to update class variables, no need to rewrite methods
    num = 20 #for roll method
    string = 'Twenty' #for repr method

class Cup:
    '''class that stores Cup objects.
    composed of the Dice classes'''

    #class var needed for repr later
    string = ''

    #initialize at 1 default for each dice
    def __init__(self,six=1,ten=1,twenty=1):
        self.dice = []
        self.six = six
        self.ten = ten
        self.twenty = twenty

        #append dice list with total number of dice user requires
        for i in range(self.six):
            self.dice.append(SixSidedDie())
        for j in range(self.ten):
            self.dice.append(TenSidedDie())
        for k in range(self.twenty):
            self.dice.append(TwentySidedDie())

        #raise error if user inputs 0 for all dice
        if len(self.dice) == 0:
            raise NoDiceError('No dice to roll in the cup.')

    def roll(self):
        self.res = 0
        for i in self.dice: #iterate through each type of die and roll
            self.res += i.roll() #add to final result
            self.string += str(i) + ',' #add for the repr
        return self.res

    def getSum(self):
        return self.res

    #need to raise error if cup is empty
    def __repr__(self):
        return f'Cup({self.string[:-1]})'


class NoDiceError(Exception):
    '''Used to check whether user forgets to include
    dice to roll with their cup'''
    pass
