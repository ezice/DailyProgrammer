import sys

# Read each line of input
# Break into eight character groups
# Convert eight character string to its character
# Place character in output buffer
# At EOF, output buffer

def outputBuffer = ''

for line in sys.stdin:
    #
    # Parse the input
    #

    print('line = ' + line)

    def linePosition = 0
    def workInt

    while (linePosition < len(line)):
        workInt = 0

        for i in range(8):
            workInt = workInt * 2 + string.atoi(line[linePosition])

        outputBuffer.append(chr(workInt))

print(outputBuffer)
quit()
