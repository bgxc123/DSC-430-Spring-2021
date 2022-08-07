#Name: Brendan Gee
#Date: 5/31/21
#Video Link: https://youtu.be/kwozHoU018A
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.

import numpy as np
import matplotlib.pyplot as plt
import random

def conway(s,p):
    '''generates a 2-D numpy array board, with
    dimensions s x s and randomly populated with
    probability p'''

    #create lst with 1s & 0s based on p
    res = []
    for i in range(s**2):

        if p >= random.random():
            res.append(1)
        else:
            res.append(0)

    #turn res into an nparray, resize
    res = np.array(res)
    res = res.reshape(s,s)
    return res

def advance(b,t):
    '''advances a conway board, b, t number of times
    based on a set of rules'''
    counter = 0
    s = int(b.size**(1/2))

    #print original board position
    printSummary(b,s,counter)

    while counter < t:
        
        #count live neighbors for each cell
        c = liveNeighbors(b)

        #based on each cells adjacent live neighbors, determine new value of cell
        b = newVals(b,c)

        #print out new board position, add 1 to counter
        printSummary(b,s,counter+1)
        counter += 1

def liveNeighbors(b):
    '''takes in a conway board and returns the
    number of live adjacent cells per cell'''

    res = []
    length = int(b.size**(1/2))

    #take the b[i][j] index and sum each adjacent cell to get # of live cells
    for i in range(len(b)):
        for j in range(len(b[i])):
            
            #use module to adjust for torus shape
            res.append(b[i][(j-1) % length] + b[(i-1) % length][j] + b[(i+1) % length][j] + b[i][(j+1) % length] +
                       b[(i+1) % length][(j-1) % length] + b[(i-1) % length][(j+1) % length] + b[(i+1) % length][(j+1) % length] +
                       b[(i-1) % length][(j-1) % length])
    return res

def newVals(b,c):
    '''given a board and count of adjacent live cells,
    calculate new value for each cell given conway rules'''
    res = []

    #convert board to list to make it easier to iterate through
    b = b.ravel()
    b = list(b)

    #calculate values to append to res based on logic
    for num in c:
        for i in range(len(b)):
            
            #dead cell reproduction
            if num == 3 and b[i] == 0:
                res.append(1)
                b.pop(i)
                break

            #live cell underpopulation
            elif num < 2 and b[i] == 1:
                res.append(0)
                b.pop(i)
                break

            #live cell overpopulation
            elif num > 3 and b[i] == 1:
                res.append(0)
                b.pop(i)
                break

            #live cell next generation
            elif b[i] == 1: #already know num has to be 2 or 3 if this case is ran
                res.append(1)
                b.pop(i)
                break

            #otherwise, dead cell with no 3 live cells => still dead
            else:
                res.append(0)
                b.pop(i)
                break

    #convert res to 2-D np array
    size = int(len(res)**(1/2))
    res = np.array(res)
    res = res.reshape(size,size)
    return res


def printSummary(b,s,c):
    '''takes in a conway board and prints out a nice
    display of the board'''
    
    b = np.flipud(b)
    mark = np.argwhere(b) #place mark for ones
    
    #fixed fig size unless the array is 50 or greater
    if s < 50:  
        plt.figure(figsize=(5,5))
    else:
        plt.figure(figsize=(s//5,s//5))
    plt.scatter(mark.T[1,:],mark.T[0,:], marker = 'o') #marks with an o when 1
    plt.axis('off') #don't need axis
    plt.title(f'Game of Life Iteration #{c} in {s}x{s} matrix') #dynamic title
    plt.show()
        

    
    
