#Name: Brendan Gee
#Date: 4/26/21
#Video Link: https://youtu.be/HunOhkzw-0c
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.

def humanPyramid(row,column):
    '''Determines the weight a person is supporting
    in a human pyramid give a row/col index'''
    weight = 0

    #base case
    if row == 0:
        return 0

    #recursion
    
    #check for edges of pyramid
    if column == 0 or column == row:
        return 64 + 1/2*(humanPyramid(row-1,0))

    #check for middle sections of pyramid
    else:
        #ppl in middle always support 2 peoples weight above divded by two (256/2)
        #ppl in middle also support aggregate weight from people above
        return 128 + 1/2*(humanPyramid(row-1,column-1)) + 1/2*(humanPyramid(row-1,column))
        
    
    

    
