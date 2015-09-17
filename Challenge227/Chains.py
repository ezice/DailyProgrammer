import sys

#
# Read dimension line.
#

# Check dimension line parameters.
# Read matrix.
# Check matrix against dimensions provided.
# Assess chains.
    # For each column in each row
        # If not blank,
            # For each existing chain,
                # If not in any
# Print answer.

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
    if (scoreLine(line.decode("utf-8"), dictionary) > 0):
        linesFound += 1
        print(line.decode("utf-8"));

    if (linesFound == 3):
        break

quit()
