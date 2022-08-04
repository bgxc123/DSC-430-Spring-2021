#Name: Brendan Gee
#Date: 4/19/21
#Video Link: https://youtu.be/skE-ojBrCoE
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

def happyPrimes():
    '''Takes a positive integer, determines if it is happy or
    sad, prime or not prime'''

    res = []

    while True:
        try:
            num = int(input("Enter a number (Anything else to Quit): "))
        except ValueError:
            break
                  
        #determine if number is prime
        res.append(isPrime(num))

        #determine if number is happy
        res.append(isHappy(num))

        #print statement
        print(printSummary(num,res))


def isPrime(num):
    '''Determines if number is prime and returns
    prime or non-prime'''

    #return prime/non-prime for base cases
    if num == 1:
        return 'non-prime'
    elif num == 2:
        return 'prime'
    
    #determine if number greater than 3 is prime
    for i in range(2,num):
        if num % i == 0:
            return 'non-prime'
        elif num - 1 == i:
            return 'prime'

def isHappy(num):
    '''Determines and returns if a number
    is happy or sad'''
    res = []

    while True:

        #Test if digits add to one
        if splitDigits(num):
            return 'happy'
        #If digits don't add to one, checks if number has already been tried
        elif num in res:
            return 'sad' #number is sad if a given iteration has already been tried
        else:
            res.append(num) #stores each num so we can check elif clause
            num = newNum(num) #generates new number from the happy calculation
            
def splitDigits(num):
    '''Takes in a number and returns True or
    False depending if the sum of squared digits
    adds up to one'''

    res = []
    for i in str(num): #can't iterate through an int, so convert to str
        res.append(int(i)**2) #convert back to int to square i and add to res
    if sum(res) == 1:
        return True
    else:
        return False


def newNum(num):
    '''Takes a list and returns a number
    with the list elements as digits'''
    res = 0

    for i in str(num): #can't iterate through an int, so convert to str
        res += int(i)**2 #convert back to int to square i and add to res
    return int(res)

def printSummary(num,result):
    '''Prints out if number is happy/sad and
    prime/non-prime'''

    return f'{num} is a {result[-2]} number and a {result[-1]} number' #since appending to a list, take the last two entries
