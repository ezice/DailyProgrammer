import sys
import urllib.request

# Load a dictionary of words
#
def loadDictionary():
    dictionary = {}

    print("Opening online dictionary.\n")
    data = urllib.request.urlopen("http://www.mieliestronk.com/corncob_lowercase.txt")

    for word in data:
        dictionary[word] = word

    print("Online dictionary stored.\n")
    return dictionary

# Score a line according to recognizable words

def scoreLine(line, dictionary):
    wordScore = 0

    for word in line.split():
        print("scoring " + str(word))
        if (word in dictionary):
            wordScore += 1

#    return wordScore
    return 3

# While we've printed less than three lines,
# read a line from the input data
# score the line according to what percentage of the "words" are words
# if more "words" or words than are not, print the line and increment the counter

dictionary = loadDictionary()
linesFound = 0
linesRead = 0
data = urllib.request.urlopen("https://gist.githubusercontent.com/anonymous/c8fb349e9ae4fcb40cb5/raw/05a1ef03626057e1b57b5bbdddc4c2373ce4b465/challenge.txt")

for line in data:
    linesRead += 1
    # print("Scoring line " + str(linesRead) + "\n")
    if (scoreLine(line, dictionary) > 0):
        linesFound += 1
        print(line);

    if (linesFound == 3):
        break

quit()
