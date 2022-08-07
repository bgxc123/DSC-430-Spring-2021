#Name: Brendan Gee
#Date: 5/20/21
#Video Link: https://youtu.be/wUaKOtBJ-Qs
#Honor Statement: I have not given or received any unauthorized assistance on this assignment.

import math
import War_Random_Numbers

class Point:
    '''class to make a point with x & y coordinates'''

    def __init__(self,x=0,y=0):
        '''initialize point obj at user given values'''
        
        self.x = x
        self.y = y
        

    def setx(self,xcoord):
        '''set the x coordinate'''
        
        self.x = xcoord

    def sety(self,ycoord):
        '''set the y coordinate'''
        
        self.y = ycoord

    def getx(self):
        '''returns x coordinate'''
        return self.x

    def gety(self):
        '''returns y coordinate'''
        return self.y

    def __repr__(self):
        '''return representation of point obj'''

        return f'Point({self.x},{self.y})'


class Ellipse:
    '''composed of point class to take in two focal points,
    and also takes in a width value, which is the distance
    of the long part of the ellipse'''

    def __init__(self,p1=(0,0),p2=(0,0),w=2):
        '''initialize ellipse obj at user given values'''

        #initialize point objs & width
        self.p1 = p1
        self.p2 = p2
        self.w = w

    def getx(self):
        '''gets both x values in the ellipse'''
        return self.p1[0], self.p2[0]

    def gety(self):
        '''gets both y values in the ellipse'''
        return self.p1[1], self.p2[1]

    def getw(self):
        '''gets the width of the ellipse'''
        return self.w

    def inEllipse(self,p):
        '''returns True if point is in ellipse,
        False otherwise'''

        #distance between first focal point and p
        l1 = math.sqrt((self.p1[0] - p[0])**2 + (self.p1[1] + p[1])**2)

        #distance between second focal point and p
        l2 = math.sqrt((self.p2[0] - p[0])**2 + (self.p2[1] + p[1])**2)

        #if added lengths longer than w, outside of ellipse
        if l1 + l2 <= self.w:
            return True
        else:
            return False

def computeOverlapOfEllipses(e1,e2):
    '''takes two ellipse objects and returns the area of overlap
    if there is any'''

    #create a box around the ellipses
    l = leftBottom(e1.getx(),e2.getx(),e1.getw(),e2.getw())
    r = rightTop(e1.getx(),e2.getx(),e1.getw(),e2.getw())
    b = leftBottom(e1.gety(),e2.gety(),e1.getw(),e2.getw())
    t = rightTop(e1.gety(),e2.gety(),e1.getw(),e2.getw())

    #area of box
    a = boxArea(l,r,b,t)

    #generate points inside box based on box constraints
    xScaleFactor = r - l
    yScaleFactor = t - b

    xShiftFactor = l
    yShiftFactor = b

    #points to generate
    num = 50000

    pointLst = generatePoints(xScaleFactor,yScaleFactor,xShiftFactor,yShiftFactor,num)

    #given the points, calculate the area shared between ellipses
    res = calcArea(a,pointLst,e1,e2)

    return res

def leftBottom(t1,t2,w1,w2):
    '''Given two tuples of x/y values, find the
    minimum value and and the max width'''

    res = 0

    #get min of tuple values
    m = min(t1+t2)

    #determine which ellipse width is longer
    if w1 >= w2:
        res += m - w1
    else:
        res += m - w2

    return res

def rightTop(t1,t2,w1,w2):
    '''Given two tuples of x/y values, find the
    maximum value and and the max width'''

    res = 0

    #get max of tuple values
    m = max(t1+t2)

    #determine which ellipse width is longer
    if w1 >= w2:
        res += m + w1
    else:
        res += m + w2

    return res

def boxArea(l,r,b,t):
    '''given the coordinate values of a box,
    find the area'''

    #calculate length & width
    length = t - b
    width = r - l

    #calculate area
    a =  length * width

    return a

def generatePoints(xScaleFactor,yScaleFactor,xShiftFactor,yShiftFactor,num):
    '''giving scaling & shifitng factors, generates a number of random points
    using a PRNG'''

    res = []

    #create War & Peace PRNG obj
    x = War_Random_Numbers.WarAndPeacePseudoRandomNumberGenerator()

    #set different seed for different random numbers
    y = War_Random_Numbers.WarAndPeacePseudoRandomNumberGenerator(3000)
    
    #generate num random points
    xRandLst = x.generate(num)
    yRandLst = y.generate(num)

    #append each random point to the resulting list using scale/shift factors
    for rand1 in xRandLst:
        for rand2 in range(len(yRandLst)):
            res.append((xScaleFactor * rand1 + xShiftFactor,yScaleFactor * yRandLst[rand2] + yShiftFactor))
            yRandLst.pop(rand2) #pop index so the value isn't repeated
            break #break to start with new char in xRandLst

    return res
        
def calcArea(a,pointLst,e1,e2):
    '''given random points in a box, calcs the estimated area
    shared by each ellipse'''

    #counter for times a random point lands in both ellipses
    inEllipses = 0
    
    for point in pointLst:
        
        #if a point lands in both ellipses, add to counter
        if e1.inEllipse(point) and e2.inEllipse(point):
            inEllipses += 1

    #estimate area based on area of box & % of points inside both ellipses
    res = inEllipses/len(pointLst) * a

    return res 
