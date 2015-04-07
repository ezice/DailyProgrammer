import sys

# Read each line of input
# Break into eight character groups
# Convert eight character string to its character
# Place character in output buffer
# At EOF, output buffer

def getNextCharacter():
    # Read eight characters from stdin
    # Convert to int
    # Convert to ASCII character and return
    binaryCounter = 0
    intValue = 0

    while (binaryCounter < 8):
        binaryCharacter = sys.stdin.read(1)

        if (binaryCharacter == ''):
            return ''
        elif (binaryCharacter == '\n'):
            continue

        intValue = (intvalue * 2) + int(binaryCharacter)
        binaryCounter += 1

    return chr(intValue)

while (True):
    character = getNextCharacter()

    if (character == ''):
        print
        break

    print(character, end='')
quit()
