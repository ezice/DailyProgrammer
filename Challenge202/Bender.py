import sys

# Read each line of input
# Break into eight character groups
# Convert eight character string to its character
# Place character in output buffer
# At EOF, output buffer

outputBuffer = ''

for line in sys.stdin:
    #
    # Parse the input
    #

    print('line = ' + line)

    linePosition = 0

    while (linePosition < len(line)):
        workInt = 0

        for i in range(8):
            workInt = workInt * 2 + int(line[linePosition])

        outputBuffer += chr(workInt)

print(outputBuffer)
quit()
