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
    [" _ "," "," _ "," _ ","   "," _ "," _ "," _ "," _ "," _ "],
    ["| |","|"," _|"," _|","|_|","|_ ","|_ ","  |","|_|","|_|"],
    ["|_|","|","|_ "," _|","  |"," _|","|_|","  |","|_|"," _|"]
    ]


    print('in call: length lines = ' + str(len(lines)))
    for line in lines:
        outputLines = ["", "", ""]

        for digit in line:
            print('digit = ' + digit)
            for i in range(3):
                outputLines[i] += bankNumber[i][int(digit)]

        for outputLine in outputLines:
            print(outputLine)


lines = []

for line in sys.stdin:
    #
    # Parse the input
    #

    print('line = ' + line)

    i = 0
    for pline in lines:
        print('lines[' + str(i) + '] = ' + pline)
        i += 1

    if len(lines) < 3:
        lines += parseInput(line.rstrip('\n'))
    elif len(lines) == 3:
        if line.rstrip('\n') != '':
            usage()
            quit()

        break

#
# Build the output
#
print('before call: length lines = ' + str(len(lines)))
displayOutput(lines)
quit()
