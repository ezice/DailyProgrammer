import sys
from enum import Enum

# Define Card enum
class Card(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

# Define Suit enum


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

        intValue = (intValue * 2) + int(binaryCharacter)
        binaryCounter += 1

    return chr(intValue)

while (True):
    character = getNextCharacter()

    if (character == ''):
        print
        break

    print(character, end='')

print('\n')
quit()
