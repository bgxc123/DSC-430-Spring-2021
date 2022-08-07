#Name: Brendan Gee
#Date: 5/12/21
#Video Link: https://youtu.be/TlPXEzdiY98
#Honor Statement: I have not given or received any unauthorized assistance on this assignment


#imports used
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser

#global variables - needed for recursion/final answer
visited = set()
res = {}


def Surf_CDM(url):
    '''Takes a url and crawls webpages to find the 25 most frequent words'''

    global visited #keep track of each url - don't crawl a site more than once
    visited.add(url)
    
    #store links and words
    links,words = analyze(url) 

    #append words to global res
    global res
    res = appendDict(res,words)

    #try links
    for link in links:

        #check if link has already been visited
        if link not in visited:
            try:
                Surf_CDM(link)
            except:
                pass


def analyze(url):    
    '''Takes in a url and returns the links as well as the words'''

    #read url, feed it into HTMLParser subclass
    content = urlopen(url).read().decode()
    collector = Collector()
    collector.feed(content)

    #Get the links and words
    urls = collector.getLinks()
    words = frequency(collector.getWords())

    return urls,words


class Collector(HTMLParser):
    '''Extends HTMLParser class to include getting links
    and word count'''

    #tag list to parse through for collecting words
    wordTagLst = ['a','p','h1','h2','h3','h4','h5','h6']

    #initalize super class and instance variables
    def __init__(self):
        '''Initialize list to store links'''
        HTMLParser.__init__(self)
        self.links = []
        self.words = ''
        self.res = ''

    def handle_starttag(self, tag, attrs):
        '''append links to self.links'''
        if tag == 'a': #link tag

            for attr in attrs:
                if attr[0] == 'href':
                    
                    #append link if it's within a restricted subset of webpages
                    if  attr[1][:18] == 'https://law.depaul':
                        
                        self.links.append(attr[1])

                    #for relative links - had trouble appending
                    elif attr[1][-3:] != 'pdf': #don't want to check pdfs
                        
                        #url join to make relative links absolute links
                        if urljoin('https://law.depaul.edu',attr[1])[:18] == 'https://law.depaul':
                            self.links.append(urljoin('https://law.depaul.edu',attr[1]))
                            
        #start appending words if tag is in set tag list
        if tag in self.wordTagLst:
                self.words = True

    def handle_data(self,data):
        '''handles data within tags'''
        
        if self.words == True: #if starttag is in tag list, append to self.res
            self.res += data


    def handle_endtag(self,tag):
        '''what to do after endtag'''

        #once a tag is closed, no longer append
        if tag in self.wordTagLst:
            self.words = False

    #method to return links
    def getLinks(self):
        '''returns list of links'''
        return self.links

    #method to return words
    def getWords(self):
        '''returns the word freq'''
        return self.res

def frequency(data):
    '''does a word count given a string input
    and returns a dictionary with the frequencies'''

    res = {}

    #list of words to ignore
    stopLst = ['a','an','and','are','as','at','be','by','for','from','has','he','in','is','it','its','of','on','that','the','to','was','were','with','will','she','but','aba','turn','resourcecampus','resourceuniversity','resourceinformation','calendaracademic','centraldesire2learn','emailuniversity','foralumni','friendscurrent']

    #remove punctuation - only want to capture words
    table = str.maketrans('/?.>,<";:|]}[{+=-_)(*&^%$#@!~`', 30*' ')
    data = data.translate(table)

    #split data
    data = data.lower().split()

    #append to dictionary if word is valid
    for word in data:
        if word in stopLst or len(word) <= 2 or len(word) > 20:
            continue
        elif word in res:
            res[word] += 1
        else:
            res[word] = 1

    return res
    

def topWords(d):
    '''returns the top 25 words in a dictionary'''

    #store keys and values in lists
    keys = list(d.keys())
    vals = list(d.values())
    counter = 0

    while counter < 25: #want the 25 most frequent
        m = max(vals)
        i = vals.index(m) #retrieve max val index
        print('{:20} {:8}'.format(keys[i], m)) #return key/value at the max

        #pop key and value, add 1 to counter
        keys.pop(i)
        vals.pop(i)
        counter += 1


def appendDict(res,words):
    '''appends temp dictionary to a master dictionary'''

    for word in words:
        if word in res:
            #if word already in dictionary, add the frequencies
            res[word] += words[word]
        else:
            #if word not in dictionary, add the key,value pair 
            res.update({word: words[word]})

    return res
