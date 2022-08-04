#Name: Brendan Gee
#Date: 4/4/21
#Video Link: https://youtu.be/0iJ9qNPNiZU
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.

def coprime(a,b):
    '''function tests whether two integers are coprime, or where their greatest
    common divsior equals one'''

    #Euclidean Algorithm
    while a > 1 and b > 1: #avoid modulo division by zero error
        if a > b:
            a = a % b
        elif b > a:
            b = b % a
        else:
            break
        
    #coprime when gcd(a,b) = 1
    if a == 1 or b == 1:
        return True
    else:
        return False
        

def coprime_test_loop():
    '''function that asks user for two numbers and determines if they are
    coprime or not. returns result and gives user option to quit or ask for
    new pair of numbers'''

    userInput = ''
    print('Use this function to test if two numbers are coprime!')

    while userInput != 'QUIT':
        
        #avoiding user error types
        try: 
            
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))

        except ValueError:
            print('Make sure to choose two integers!')
            continue #resets loop if except error is executed

        #positive integers only
        if num1 < 0 or num2 < 0:
            print('Use positive integers only!')
            continue

        #using coprime function
        if coprime(num1,num2) == True:
            print(f'The numbers {num1} and {num2} are coprime.')
        else:
            print(f'The numbers {num1} and {num2} are NOT coprime.')
            
        #option for user to quit or try again
        userInput = input('Hit "ENTER" to try again. Type "QUIT" to exit. ')
    
            

