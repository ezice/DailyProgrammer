import sys

#
# Read dimension line.
#
inline = raw_input()

#
# Split the dimensions
#
lines = inline.split()[0]
columns = inline.split()[1]

#
# Read matrix.
#
def matrix = []

for line in raw_input():
    matrix.append(line)

# Assess chains.
def chains = []

# For each column in each row
vPos = 0;
def lastLine;

for line in matrix:
    hPos = 0;

    for char in line:
        # If not blank, look up and back to see if any neighbors are in chains yet.
        if (char == 'x'):
            if (hPos > 0):
                if (line[hPos - 1] == 'x'):
                    chain = findChainWithPoint(new Point(vPos, hPos - 1))
                    chain.addPoint(new Point(vPos, hPos))
                # For each existing chain,
                    # If not in any


# Check matrix against dimensions provided.

# Print answer.
quit()
