import sys
import re

def usage():
    print("usage: each entry must be four lines long of the format:")
    print("111111111 (nine digits)")
    print("222222222")
    print("333333333")
    print("<blank line>")

def parseInput(inputLine):
    def bankNumber = [
    [" "," _ "," _ ","   "," _ "," _ "," _ "," _ "," _ "],
    ["|","  |","  |","| |","|  ","|  ","  |","| |","| |"],
    [" "," _ "," _ "," _ "," _ "," _ ","   "," _ "," _ "],
    ["|","|  ","  |","  |","  |","| |","  |","| |","  |"],
    [" "," _ "," _ ","   "," _ "," _ ","   "," _ "," _ "]
    ]

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

    return terms[0]

def displayOutput(terms):
    displayWidth = displayEquation(terms)
    displayCarry(terms, displayWidth)

for line in sys.stdin:
    #
    # Parse the input
    #
    terms = parseInput(line.rstrip('\n'))

    #
    # Build the output
    #
    displayOutput(terms)
