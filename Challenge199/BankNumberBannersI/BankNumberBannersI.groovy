import sys
import re

def usage():
    print("usage: each entry must be four lines long of the format:")
    print("111111111 (nine digits)")
    print("222222222")
    print("333333333")
    print("<blank line>")

def parseInput(inputLine):
    #
    # Validate the input: Must have a single argument of the form NNNNNNNNN
    #
    match = re.match("\d[9]", inputLine)

    if terms is None:
        usage()
        quit()

    return inputLine

def displayOutput(lines):
    def bankNumber = [
    [" "," _ "," _ ","   "," _ "," _ "," _ "," _ "," _ "],
    ["|","  |","  |","| |","|  ","|  ","  |","| |","| |"],
    [" "," _ "," _ "," _ "," _ "," _ ","   "," _ "," _ "],
    ["|","|  ","  |","  |","  |","| |","  |","| |","  |"],
    [" "," _ "," _ ","   "," _ "," _ ","   "," _ "," _ "]
    ]

    for line in lines:
        

def lines = []

for line in sys.stdin:
    #
    # Parse the input
    #
    if len(lines) < 3:
        lines += parseInput(line.rstrip('\n'))
    else if len(lines) == 3:
        if line.rstrip('\n') != '':
            usage()
            quit()

        break

    #
    # Build the output
    #
    displayOutput(lines)
