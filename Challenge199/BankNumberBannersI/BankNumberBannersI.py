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
    match = re.match("\d{9}", inputLine)

    if match is None:
        usage()
        quit()

    return inputLine

def displayOutput(lines):
    bankNumber = [
    [" _ ","   "," _ "," _ ","   "," _ "," _ "," _ "," _ "," _ "],
    ["| |"," | "," _|"," _|","|_|","|_ ","|_ ","  |","|_|","|_|"],
    ["|_|"," | ","|_ "," _|","  |"," _|","|_|","  |","|_|"," _|"]
    ]


    for line in lines:
        outputLines = ["", "", ""]

        for digit in line:
            for i in range(3):
                outputLines[i] += bankNumber[i][int(digit)]

        for outputLine in outputLines:
            print(outputLine)


lines = []

for line in sys.stdin:
    #
    # Parse the input
    #

    i = 0
    for pline in lines:
        i += 1

    if len(lines) < 3:
        lines.append(parseInput(line.rstrip('\n')))
    elif len(lines) == 3:
        if line.rstrip('\n') != '':
            usage()
            quit()

        break

#
# Build the output
#
displayOutput(lines)
quit()
