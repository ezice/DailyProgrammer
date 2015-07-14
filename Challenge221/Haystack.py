import sys

# Load a dictionary of words
#
def loadDictionary():
    dictionary = {}

    data = urllib2.urlopen("http://www.mieliestronk.com/corncob_lowercase.txt")

    for word in data:
        dictionary[word] = word

    return dictionary

# Score a line according to recognizable words

def scoreLine(line, dictionary):
    wordScore = 0

    for word in line:
        if (word in dictionary):
            wordScore++

    return wordScore

# While we've printed less than three lines,
# read a line from the input data
# score the line according to what percentage of the "words" are words
# if more "words" or words than are not, print the line and increment the counter

dictionary = loadDictionary()
linesFound = 0
data = urllib2.urlopen("https://gist.githubusercontent.com/anonymous/c8fb349e9ae4fcb40cb5/raw/05a1ef03626057e1b57b5bbdddc4c2373ce4b465/challenge.txt")

for line in data:
    if (scoreLine(line, dictionary) > 0):
        linesFound++
        print(line);

    if (linesFound == 3):
        break
        
quit()
