import sys

class Point():
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def getXpos(self):
        return self.xPos

    def getYpos(self):
        return self.yPos

chains = []

def findChainWithPoint(point):
    for chain in chains:
        for cpoint in chain:
            if ((cpoint.getXpos() == point.getXpos()) and
                (xpoint.getYpos() == point.getYpos())):
                return chain
    return None
#
# Read dimension line.
#
inline = input()

#
# Split the dimensions
#
lines = inline.split()[0]
columns = inline.split()[1]

#
# Read matrix.
#
matrix = []

for line in input():
    matrix.append(line)

# Assess chains.

# For each column in each row
vPos = 0
lastLine = None

for line in matrix:
    hPos = 0;

    for char in line:
        # If not blank, look up and back to see if any neighbors are in chains yet.
        if (char == 'x'):
            if (hPos > 0):
                if (line[hPos - 1] == 'x'):
                    chain = findChainWithPoint(Point(vPos, hPos - 1))

                    if (chain == None):
                        print("Error: found point in current line, but no chain.")
                        quit(1)
                    else:
                        chain.append(Point(vPos, hPos))
            elif (vPos > 0):
                if (lastLine[hPos] == 'x'):
                    chain = findChainWithPoint(Point(vPos - 1, hPos))

                    if (chain == None):
                        print("Error: found point in previous line, but no chain.")
                        quit(2)
                    else:
                        chain.append(Point(vPos, hPos))
            else:
                chain = [Point(vPos, hPos)]
                chains.append(chain)

        hPos += 1

    vPos += 1
    lastLine = line
print(len(chains))
# Print answer.
quit()
