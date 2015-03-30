import sys

# Read each line of input
# Break into eight character groups
# Convert eight character string to its character
# Place character in output buffer
# At EOF, output buffer

outputBuffer = ''
lines = []

for line in sys.stdin:
    #
    # Parse the input
    #
    lines.append(line)

linePosition = 0
for lineCounter in range(lines.size()):

    while (linePosition < len(line)):
        workInt = 0

        for i in range(8):
            if (lines[lineCounter][linePosition] == '\n'):
                

            workInt = workInt * 2 + int(line[linePosition])
            linePosition += 1

        outputBuffer += chr(workInt)

print(outputBuffer)
quit()
