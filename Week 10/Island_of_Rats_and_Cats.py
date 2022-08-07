#Name: Brendan Gee
#Date: 6/11/21
#Video Link: https://youtu.be/fvuQR6-8-ko
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

import random
from matplotlib import pyplot as plt
import numpy as np
import Parameters

def islandOfRatsAndCats():
    '''Simulates 10000 days on the island and displays the
    results'''

    berry_ttl = Berry(1,Parameters.berry_ttl)
    r = Rat(Parameters.rat_ttl)
    c = Cat(Parameters.cat_ttl)
    day = 1
    res_days = []
    res_berries = []
    res_rats = []
    res_cats = []
    res_rainfall = []

    while day <= Parameters.simulation_days:

        #check for rain, returns rain on a given day in mm
        rain = rainCheck(Parameters.rain_chance,Parameters.rain_mean,Parameters.rain_std)

        #calculate number of berries based on the rain
        berries = berryCount(rain,Parameters.berry_coefficient,Parameters.island_size)
        
        #create berry object, add to ttl dictionary
        b = Berry(day,berries)
        berry_ttl.add(b)

        #rats eat berries, cats eat rats
        r.eat(berry_ttl)
        c.eat(r)

        #check for birth
        r.birth()
        c.birth()

        #check for death/starvation
        berry_ttl.perishCheck(day)
        r.perishCheck()
        c.perishCheck()

        #print summary of the day now that it's over
        printSummary(day,rain, berry_ttl, r, c)

        #append to lists for time series graphs
        res_days.append(day)
        res_rainfall.append(rain)
        res_berries.append(sum(berry_ttl.getValues()))
        res_rats.append(r.getObjs())
        res_cats.append(c.getObjs())

        #next day => add 1 to day
        day += 1

        #adding days to each object
        berry_ttl.addDay()
        r.addDay(1)
        c.addDay(1)

    return res_days, res_rainfall, res_berries, res_rats, res_cats


def rainCheck(p,mean,sd):
    '''determines if there is rain on a given day
    on the island'''
    
    
    if p >= random.random():
        return randRainfall(mean,sd)[0]
    else:
        return 0

def randRainfall(mean,sd):
    '''generates a random amount of rainfall based on
    a mean of 25mm and sd of 5mm with a normal dist'''

    res = np.random.normal(mean,sd,1)
    
    return res

def berryCount(r,bC,iS):
    '''calculates the # of berries produced from
    the rainfall, berry coefficent, and island size'''

    res = r * bC * iS

    return int(res)
        

class Berry:
    '''Object that stores dict of berries with the
    number of days they've had'''


    def __init__(self,day=1,objects=0):
        '''initializes the object'''

        self.objects = objects
        self.day = day

        if self.objects == 0:
            self.res = {}

        else:
            self.res = {self.day:self.objects}

    def __repr__(self):
        return f'Berry({self.res})'

    def getValues(self):
        '''returns the number of values in the object'''
        vals = []

        for key in self.res:
            vals.append(self.res[key])

        return vals

    def getDays(self):
        '''returns the number of days in the object'''
        
        keys = []

        for key in self.res:
            keys.append(key)
            
        return keys

    def getBoth(self):
        '''returns a dictionary of Day/Value pair'''

        return self.res

    def addDay(self):
        '''adds a day to the dictionary to track
        berry days'''

        temp = {}
        for key in self.res:
            temp.update({key+1:self.res[key]})

        self.res = temp

        return self.res

    def add(self,other):
        '''adds an object pairing to an existing object dict'''

        for key in other.res:
            if key in self.res.keys():
                self.res[key] += other.res[key]
            else:
                self.res.update({key:other.res[key]})

        return self

    def subtractBerry(self,ind):
        '''takes away one berry from a given key,
        pops key/value if it is the last berry'''
        

        if self.res[ind] == 1:
             
             
            self.res.pop(ind)
             
        else:
            self.res[ind] -= 1
        
        

    def perishCheck(self,day):
        '''checks if any of the berries on the island
        perish due to aging'''

        for key in self.res:
            if day - key == 10:
                self.res.pop(key)
                break #can't have more than 1 set of berries perish

        return self.res

class Rat:
    '''Object that stores rats in a dictionary where
    the key is days not eaten, age, and berries eaten,
    and values are the # of rats'''

    def __init__(self,objs=10):
        '''initializes rat variable'''

        self.objs = objs
        #store rats not eating after 3 days
        self.res = {}
        

        #generate the ages for each rat
        for rat in range(self.objs):

            #generate rand uniform distro of ages
            rand = random.randrange(1,Parameters.rat_age+1)

            #add rats to res and count freq by day
            if len(self.res) == 0:
                self.res.update({0:{rand:{0:1}}})
                                
            elif rand in self.res[0]:
                self.res[0][rand][0] += 1
            else:
                self.res[0][rand] = {0:1}

    def __repr__(self):
        '''representation of the obj'''

        return f'Rat({self.res})'

    def getDaysNotEaten(self):
        '''returns all keys in a list'''
        lst = []

        for i in self.res.keys():
            lst.append(i)

        return lst

    def getAges(self,ind):
        '''returns age keys in a list'''

        lst = []

        for i in self.res[ind]:
                lst.append(i)

        return lst

    def getBerriesEaten(self,ind1,ind2):
        '''returns berries eaten keys in a list'''
        lst = []

        for i in self.res[ind1][ind2]:    
            lst.append(i)
        return lst

    def getObjs(self):
        '''returns sum of all objs in a list'''

        lst = []

        for i in self.res:
            for j in self.res[i]:
                for k in self.res[i][j]:
                    
                    lst.append(self.res[i][j][k])

        return sum(lst)

    def subtractObj(self,ind1,ind2,ind3):
        '''takes away one rat from a given
        key/value pair. pops if none left after'''

        if self.res[ind1][ind2][ind3] == 1:
            if len(self.res[ind1][ind2]) == 1:
                self.res[ind1].pop(ind2)
            else:
                self.res[ind1][ind2].pop(ind3)

        else: self.res[ind1][ind2][ind3] -= 1

    def addObj(self,ind1,ind2,ind3,num):
        '''adds a obj to a new dict key/value pair'''

        if num == 0:
            pass

        elif ind1 not in self.res:
            
            self.res[ind1] = {ind2:{ind3:num}}

        elif ind2 not in self.res[ind1]:
            
            self.res[ind1][ind2] = {ind3:num}

        elif ind3 not in self.res[ind1][ind2]:
            self.res[ind1][ind2][ind3] = num
        
        else:
            
            self.res[ind1][ind2][ind3] += num

    def noFood(self):
        '''adds a day to not eating'''

        temp = {}

        for key in self.res:
            temp.update({key+1:self.res[key]})
        self.res = temp

        return self.res

    def getDict(self):
        '''returns dictionary of obj'''

        return self.res
    
    def eat(self,berries):
        '''rat chosen at random will try to eat a berry
        if available on the island'''

        temp = Rat(0)

        #while there are still berries and rats left to eat...
        while sum(berries.getValues()) > 0 and self.getObjs() > 0:
            try:
                
                #pick a random berry for a random rat to eat
                i,j,k = randDictInd(self)
                l = random.choice(berries.getDays())
                
            except IndexError:
                continue
            
            #add to temp
            temp.addObj(0,j,k+1,1)

            #subtract selected index from self
            self.subtractObj(i,j,k)

            #subtract berry count
            berries.subtractBerry(l)


        #if berries ran out, append the rest of self.res to temp
        if sum(berries.getValues()) == 0:

            #add a day of no eating
            self.noFood()

            #append to temp
            for key1 in self.getDict():
                for key2 in self.getDict()[key1]:
                    for key3 in self.getDict()[key1][key2]:
                        
                    
                        temp.addObj(key1,key2,key3,self.getDict()[key1][key2][key3])

        self.res = dict(temp.res)

        return self

    def addDay(self):
        '''adds a day to a rats age'''
        
        temp = {}
        
        for keys in self.res:
            for key in self.res[keys]:
                if keys not in temp:
                    temp.update({keys:{}})
                    temp[keys].update({key+1:self.res[keys][key]})
                else:
                     
                    temp[keys].update({key+1:self.res[keys][key]})
        self.res = dict(temp)

        return self.res
            

    def perishCheck(self):
        '''if rat hasn't eaten in 3 days, it dies, or if
        it is over 50 it has a chance to die'''

        temp = Rat(0)
        
        #check for any cats that haven't ate for 5 days
        if Parameters.rat_starve in self.res:
            self.res.pop(Parameters.rat_starve)

        #check for any cats over 2000 days old
        for key1 in self.res:
            for key2 in self.res[key1]:
                #if older than 2000, chance of dying
                    if key2 >= Parameters.rat_old:
                        for key3 in self.res[key1][key2]:
                            p = .05 + (key2 - Parameters.rat_old)*.05

                            if p >= random.random():
                                
                                #only add obj to temp if there is more than 1
                                #if self.res[key1][key2][key3] > 1:
                                    
                                temp.addObj(key1,key2,key3,1)

        #append self.res to temp
        for key1 in self.res:
            for key2 in self.res[key1]:
                for key3 in self.res[key1][key2]:
                    if key1 in temp.res and key2 in temp.res[key1] and key3 in temp.res[key1][key2]:
                        continue
                    else:

                        temp.addObj(key1,key2,key3,self.getDict()[key1][key2][key3])
                    
        self.res = dict(temp.res)
        return self
    def addDay(self,num):
        '''adds day specified to each rats age'''

        temp = Rat(0)

        for key1 in self.res:
            for key2 in self.res[key1]:
                for key3 in self.res[key1][key2]:
                    
                    temp.addObj(key1,key2+num,key3,self.res[key1][key2][key3])

        self.res = dict(temp.res)

        return self.res

    def birth(self):
        '''checks if a obj will give birth depending
        on how many berries it has eaten'''

        temp = Rat(0)
        
        for key1 in self.res:
            for key2 in self.res[key1]:
                for key3 in self.res[key1][key2]:

                    #if berries aten are 10 or greater
                    if key3 >= Parameters.rat_litter_first:
                        if key3 == Parameters.rat_litter_first:
                            for num in range(self.res[key1][key2][key3]):
                                

                                #add 6 - 10 rats to the obj
                                temp.addObj(0,1,0,random.randrange(Parameters.rat_litter_min,Parameters.rat_litter_max+1))
                            
                        #every 8 berries after the first 10
                        elif (key3 - 10) % Parameters.rat_litter_next == 0:

                            temp.addObj(0,1,0,random.randrange(Parameters.rat_litter_min,Parameters.rat_litter_max+1))

        #concatenate updated dictionary with new births
        for i in temp.res:
            for j in temp.res[i]:
                for k in temp.res[i][j]:
                    self.addObj(i,j,k,temp.res[i][j][k])

        return self.res
    
                    

                        
def randDictInd(r):
    '''takes in a nested dictionary, returns
    two key indices at random'''
    
    i = random.choice(r.getDaysNotEaten())
    j = random.choice(r.getAges(i))
    k = random.choice(r.getBerriesEaten(i,j))

    return i,j,k

class Cat(Rat):
    '''Creates a cat object that inherits the same properties
    from rat'''

    def __init__(self,objs=10):
        '''initializes cat obj'''

        self.objs = objs
        
        self.res = {}
        
        #generate the ages for each cat
        for rat in range(self.objs):

            #generate rand uniform distro of ages
            rand = random.randrange(1,Parameters.cat_age+1) * Parameters.cat_exp

            #add rats to res and count freq by day
            if len(self.res) == 0:
                self.res.update({0:{rand:{0:1}}})
                                
            elif rand in self.res[0]:
                self.res[0][rand][0] += 1
            else:
                self.res[0][rand] = {0:1}

    def __repr__(self):
        '''representation of cat obj'''

        return f'Cat({self.res})'


    def eat(self,r):
        '''a cat attempts eating a rat'''
        temp = Cat(0)

        #while there are still rats and cats left to eat...
        while r.getObjs() > 0 and self.getObjs() > 0:

            #pick a random rat for a random cat to eat
            try:
                
                i,j,k = randDictInd(self)
                l,m,n = randDictInd(r)
            except IndexError:
                continue

            #check if cat successfully catches rat
            if catchRat(j,r):
                
                #add to temp
                temp.addObj(0,j,k+1,1)

                #subtract selected index from self
                self.subtractObj(i,j,k)

                #subtract rat count
                r.subtractObj(l,m,n)

            else:

                #add to temp
                temp.addObj(i+1,j,k,1)

                #subtract selected index from self
                self.subtractObj(i,j,k)
                


        #if rats run out, append the rest of self.res to temp
        if r.getObjs() == 0:

            #add a day of no eating
            self.noFood()

            #append to temp
            for key1 in self.getDict():
                for key2 in self.getDict()[key1]:
                    for key3 in self.getDict()[key1][key2]:
                        
                    
                        temp.addObj(key1,key2,key3,self.getDict()[key1][key2][key3])

        self.res = dict(temp.res)

        return self

    def perishCheck(self):
        '''check whether cat will perish from starvation
        or old age'''

        temp = Cat(0)
        
        #check for any cats that haven't ate for 5 days
        if Parameters.cat_starve in self.res:
            self.res.pop(Parameters.cat_starve)

        #check for any cats over 2000 days old
        for key1 in self.res:
            for key2 in self.res[key1]:
                #if older than 2000, chance of dying
                    if key2 >= Parameters.cat_old*.015:
                        for key3 in self.res[key1][key2]:
                            p = .01 + ((key2 /.015) - Parameters.cat_old)*.001

                            if p >= random.random():
                                
                                #only add obj to temp if there is more than 1
                                #if self.res[key1][key2][key3] > 1:
                                    
                                temp.addObj(key1,key2,key3,1)

        #append self.res to temp
        for key1 in self.res:
            for key2 in self.res[key1]:
                for key3 in self.res[key1][key2]:
                    if key1 in temp.res and key2 in temp.res[key1] and key3 in temp.res[key1][key2]:
                        continue
                    else:

                        temp.addObj(key1,key2,key3,self.getDict()[key1][key2][key3])
                    
        self.res = dict(temp.res)
        return self

    def birth(self):
        '''determines if a cat can give birth based on the number of
        rats it has eaten'''
        temp = Cat(0)
        
        for key1 in self.res:
            for key2 in self.res[key1]:
                for key3 in self.res[key1][key2]:

                    #if rats ate are 50 or greater
                    if key3 >= Parameters.cat_consumption_first:
                        if key3 == Parameters.cat_consumption_first:
                            for num in range(self.res[key1][key2][key3]):
                                

                                #add 3 - 6 cats to the obj
                                temp.addObj(0,.015,0,random.randrange(Parameters.cat_litter_min,Parameters.cat_litter_max+1))
                            
                        #every 35 rats after the first 50
                        elif (key3 - 35) % Parameters.cat_consumption_next == 0:

                            temp.addObj(0,.015,0,random.randrange(Parameters.cat_litter_min,Parameters.cat_litter_max+1))

        #concatenate updated dictionary with new births
        for i in temp.res:
            for j in temp.res[i]:
                for k in temp.res[i][j]:
                    self.addObj(i,j,k,temp.res[i][j][k])

        return self.res    
        
def catchRat(age,r):
    '''determines given the rat density and cat age if the cat
    catches the rat'''

    p = (r.getObjs() / Parameters.island_size) * Parameters.rat_density / 100
    b = age / 100

    if p + b >= random.random():

        return True
    else:
        return False

def dictToLst(d):
    '''takes in a nested dictionary, returns a list'''
    lst = []

def printSummary(d,rain,b,r,c):
    '''prints out an end of day summary of the simulation'''

    if d == 1:
        print('{:10}|{:10}|{:10}|{:10}|{:10}'.format('Days','Rain','Berries','Rats','Cats'))
        print('{:10}|{:10}|{:10}|{:10}|{:10}'.format('0','0','0','10000','1000'))

    print('{:10}|{:10}|{:10}|{:10}|{:10}'.format(str(d),str(int(rain)),str(sum(b.getValues())),str(r.getObjs()),str(c.getObjs())))

def timeSeries(day,rain,berry,rat,cat):
    '''graphs each variable as a time series plot'''

    lsts = [rain,berry,rat,cat]
    ylabels = ['Rainfall (mm)','Count of Berries','Count of Rats','Count of Cats']
    title = ['Rainfall','Berries','Rats','Cats']

    for i in range(len(lsts)):

        plt.plot(day,lsts[i])
        plt.title(f'{title[i]} on the Island Simulated over 10,000 days')
        plt.xlabel('Days')
        plt.ylabel(ylabels[i])
        plt.show()

        
