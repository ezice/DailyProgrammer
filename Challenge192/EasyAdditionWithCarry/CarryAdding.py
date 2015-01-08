import sys
import re

def usage():
    print("usage: input format must be of the form X+Y[+Z]*")

def parseInput(inputLine):

    #
    # Validate the input: Must have a single argument of the form MM+NN[+OO...]
    #
    terms = re.findall("(\d+)(?:\+(\d+))+", inputLine)
    print (terms)

    if terms is None:
        usage()
        quit()

    #
    # Pad the terms on the left (right-justify).
    #
    # maxLength = getMaxLength(terms)

    # for (int i; i < inputTerms.size(); i++) {
    #     inputTerms[i] = inputTerms[i].padLeft(maxLength)
    # }

    # for term in terms

    return terms

def displayOutput(terms):
    displayWidth = displayEquation(terms)
    displayCarry(terms, displayWidth)

def displayEquation(terms):
    sum = 0

    for term in terms:
        sum = sum + term

    sumWidth = len(str(sum))

    print()

    for term in terms:
        print(str(term).rjust(sumWidth))

    print("=".rjust(sumWidth, "="))
    print(sum)
    return sumWidth

def displayCarry(terms, displayWidth):
    print("=".rjust(displayWidth, "="))

    carryString = ""
    #
    # Scan left to right.  The first position that can carry is just to the
    # right of the begining (position 1).
    for position in [1..displayWidth]:
        sum = 0
        for term in terms:
            sum = sum + term.rjust(displayWidth)[position]

        if sum == 0:
            carryString = carryString + " "
        else:
            carryString = carryString + sum

    print(carryString.rjust(displayWidth))

for line in sys.stdin:
    #
    # Parse the input
    #
    terms = parseInput(line.rstrip('\n'))

    #
    # Build the output
    #
    displayOutput(terms)
