#Name: Brendan Gee
#Date: 5/21/21
#Video Link: https://youtu.be/-WIoURGk5ag
#Honor Statement I have not given or received any unauthorized assistance on this assignment

import random
import Plot_Viewer

class SimplePlotGenerator:
    '''Once registered to a Plot Viewer, can return
    a simple plot'''
    def registerPlotViewer(self,pv):

        self.pv = pv
        
    #call from plot_viewer to print out to console
    def generate(self):
        return self.pv.viewPlot('Something happens')

class RandomPlotGenerator(SimplePlotGenerator):
    '''Generates a random plot once registered to a
    plot viewer'''
    res = []

    def generate(self):
        '''generates a random plot'''

        #create list of files to be open/read
        infiles = ['plot_names.txt','plot_adjectives.txt'
                   ,'plot_profesions.txt','plot_verbs.txt'
                   ,'plot_adjectives_evil.txt','plot_villian_job.txt'
                   ,'plot_villains.txt']

        #for each file, capture a random word
        for infile in infiles:
            infile = open(infile)
            content = infile.read().splitlines() #creates list without \n
            self.res.append(random.choice(content))
            infile.close()

        return self.pv.viewPlot(f'{self.res[-7]}, a {self.res[-6]} {self.res[-5]}, must {self.res[-4]} the {self.res[-3]} {self.res[-2]}, {self.res[-1]}')
    
class InteractivePlotGenerator(SimplePlotGenerator):
    '''Asks user for plot inputs and returns a plot'''

    res = []
    ans = []
   
    def generate(self):
        '''generates an interactive plot'''


        #create list of files to be open/read
        infiles = ['plot_names.txt','plot_adjectives.txt'
                   ,'plot_profesions.txt','plot_verbs.txt'
                   ,'plot_adjectives_evil.txt','plot_villian_job.txt'
                   ,'plot_villains.txt']

        #for each text file, select 5 random words
        for i in range(7):

            #if additional plots are generated under same instance var, replace the exisiting words
            if len(self.res) == 7: 
                self.res[i] = fiveWords(infiles[i])
            else:
                self.res.append(fiveWords(infiles[i]))

        #ask user for input based on printed list of random 5 words
        for lst in self.res:
            self.pv.viewWords(lst)
            n = self.pv.queryUser('Select a word from above (1-5): ')
            n = int(n)-1
            self.ans.append(lst[n])
            
                

        return self.pv.viewPlot(f'{self.ans[-7]}, a {self.ans[-6]} {self.ans[-5]}, must {self.ans[-4]} the {self.ans[-3]} {self.ans[-2]}, {self.ans[-1]}')          

        
def fiveWords(file):
    '''given a file, returns 5 words at random'''

    res = []
    counter = 0
    
    infile = open(file)
    content = infile.read().splitlines() #readlines without \n
    infile.close()

    while counter < 5: #append words until list is length 5
        rand = random.choice(content)
        if rand in res: #don't want to append the same word twice
            continue #reset loop so we get length 5
        else:
            res.append(rand)
            counter += 1

    return res
