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

#
# Simply find the chain index by searching all the points in all the
# chains until you find it.
#
def findChainIndexWithPoint(point):
    index = 0

    for chain in chains:
        for cpoint in chain:
            if ((cpoint.getXpos() == point.getXpos()) and
                (cpoint.getYpos() == point.getYpos())):
                return index

        index += 1
    return None

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

for line in sys.stdin:
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
                #
                # Search for chain behind us
                #
                if (line[hPos - 1] == 'x'):
                    index = findChainIndexWithPoint(Point(vPos, hPos - 1))

                    if (index == None):
                        print("vPos = ", vPos)
                        print("hPos = ", hPos)
                        print("Error: found point in current line, but no chain.")
                        quit(1)
                    #
                    # We found a chain behind us, but there might be a chain
                    # above us and our current position connects two chains.
                    #
                    elif ((vPos > 0) and (lastLine[hPos] == 'x')):
                        topIndex = findChainIndexWithPoint(Point(vPos - 1, hPos))

                        if (topIndex == None):
                            print("vPos = ", vPos)
                            print("hPos = ", hPos)
                            print("Error: found point in previous line, but no chain.")
                            quit(3)
                        else:
                            #
                            # Add the current point and the chain behind us,
                            # then delete the chain behind us.
                            chains[topIndex].append(Point)
                            chains[topIndex].extend(chains[index])
                            del chains[index]
                    else:
                        chains[index].append(Point(vPos, hPos))
                else:
                    print("New Chain. vPos = ", vPos, "; hPos = ", hPos)
                    chain = [Point(vPos, hPos)]
                    chains.append(chain)
            elif (vPos > 0):
                if (lastLine[hPos] == 'x'):
                    index = findChainIndexWithPoint(Point(vPos - 1, hPos))

                    if (index == None):
                        print("Error: found point in previous line, but no chain.")
                        quit(2)
                    else:
                        chains[index].append(Point(vPos, hPos))
            else:
                print("New Chain. vPos = ", vPos, "; hPos = ", hPos)
                chain = [Point(vPos, hPos)]
                chains.append(chain)

        hPos += 1

    vPos += 1
    lastLine = line
print(len(chains))
# Print answer.
quit()
