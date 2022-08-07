#Name: Brendan Gee
#Date: 5/17/21
#Video Link: https://youtu.be/Q-xJ1kPw6Yo
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

import random

class WarAndPeacePseudoRandomNumberGenerator():

    def __init__(self, seed=1000):
        '''initialize the object at seed 1000 default,
        open the file'''

        #initialize seed & file
        self.seed = seed
        self.infile = open('war-and-peace.txt')



    def random(self):
        
        #initialize result
        bitlst = []
        ct = 0
        rand = 0


        #record 32 pairs, and use comparsions to assign bits of 1 or 0
        while ct < 32:
            
            try:
                
                letter1 = self.infile.read(self.seed)[-1]
                letter2 = self.infile.read(100)[-1]

            #if the file goes over the index, restart 
            except IndexError:

                self.infile = open('war-and-peace.txt')
                letter1 = self.infile.read(1)[-1]
                letter2 = self.infile.read(100)[-1]

                

            #can't compare letters if they are the same
            if letter1 == letter2:
                continue 
            elif letter1 > letter2:
                bitlst.append(1)
            else:
                bitlst.append(0)

            ct += 1
            self.seed = 100

        #calculate rand based on the bitlst
        for i in range(len(bitlst)):
            
            #approaches 1, includes 0
            rand += 1/(2**(i+1))*bitlst[i]

        return rand

    def generate(self,num):
        '''generate a given number of random numbers and
        store them in a list'''
        numlst = []

        #iterate through the required # of random numbers
        for i in range(num):
            numlst.append(self.random())

        return numlst
            

    def open(self):
        '''opens file if not already open'''
        self.infile = open('war-and-peace.txt')

    def close(self):
        '''closes file'''
        
        self.infile.close()
