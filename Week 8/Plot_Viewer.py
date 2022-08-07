#Name: Brendan Gee
#Date: 5/24/21
#Video Link: https://youtu.be/A2MYHLruzeA
#Honor Statement: I have not given or received any unauthorized assistance on this assignment

import Plot_Generator

class PlotViewer:
    '''Given a plot generator, prints out
    the plot'''

    def registerPlotGenerator(self,pg):
        '''registers a plot generator for viewing'''
        self.pg = pg
        self.pg.registerPlotViewer(self) #registers instance as plot viewer to generate plots

    def viewPlot(self,string):
        '''Used to view a plot, no user input needed'''
        print(string)

    def viewWords(self,lst):
        '''Used to print out a list of words'''

        for word in lst:
            print(word)

    #used in generator classes for user input
    def queryUser(self,string):
        '''Asks the user for an input'''
        return input(string)

    def generate(self):
        '''returns plot from generator'''

        return self.pg.generate()

