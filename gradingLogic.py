#Name: Brendan Gee
#Date: 4/4/2021
#Video Link: https://youtu.be/MUSpswLQjvA
#Honor Statement:I have not given or received any unauthorized assistance on this assignment.

def zeroCheck():
    '''checks if student included all the necessary elements to not
    receive a zero on their assignment'''

    #question list to check for a zero
    qlst = ['Did the student include a single uncompressed .py file?(Y/N) ',
             'Did the student include their name?(Y/N) ',
             'Did the student include the date?(Y/N) ',
             'Did the student include a link to an unlisted 3-minute YouTube video?(Y/N) ']

    #iterating through each question
    for question in qlst:
        while True: #checking for correct user input
            res = input(question)
            if res == 'Y' or res == 'N':
                if res == 'Y':
                    break
                else:
                    return True #student automatically gets a zero
            else:
                print('Please answer "Y" or "N".')
                continue #repeats ith question

    #if requirements are met, student doesn't get a zero
    return False

def performanceCheck():
    '''checks how many points (if any) are awarded to a student iff they
    pass the zeroCheck.'''

    #initialize score at zero
    score = 0

    #question list to check for performance
    qlst = ['Out of 10 points, how would you evaluate the correctness of the code? ',
             'Out of 10 points, how would you evaluate the elegance of the code? ',
             'Out of 10 points, how would you evaluate the hygiene of the code? ',
             'Out of 10 points, how would you evaluate the discussion of the video? ']

    for question in qlst:
        while True:
            try: #verifying for integer type
                res = int(input(question))
            except ValueError:
                print('Please enter an integer between 0 and 10.')
                continue #restart loop with same question
            if res < 0 or res > 10: #check for int in correct bounds
                print('Please enter an integer between 0 and 10.')
                continue
            else:
                break #break while loop if above conditions are met
            
        score += res #add res to score and iterate to next question in for loop
            
    return score

def lateCheck():
    '''Checks if the student turned in the assignment late,
    and how many points to deduct based on the # of hours late'''

    question = "How many hours late (if any) was the student's assignment turned in? "

    while True: #check for non-int and negative values
        try:
            hrsLate = int(input(question))
            
        except ValueError: #error when res isn't int
            print('Please enter a positive integer.')
            continue #restart loop with same question
        
        if hrsLate < 0:
            print('Please enter a positive integer.')
            continue
        else:
            break #passes while loop check
        
    return .01 * hrsLate * 40 #1% for every hr late
            
        

def gradingLogic():
    '''This function is used to determine the score a student receives on
    a given assignment.'''
    
    score = 0 #initialize score at 0

    #helper function zeroCheck
    if zeroCheck() == True:
        return f"The student's score is {score}"

    #helper function performanceCheck & lateCheck
    score = performanceCheck() - lateCheck()
    if score < 0: #student can't get a negative score
        score = 0
        return f"The student's score is {score}"
    else:
        return f"The student's score is {score}"
    
        
