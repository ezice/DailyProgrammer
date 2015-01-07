import fileinput

for line in fileinput.input()
    #
    # Parse the input
    #
    terms = parseInput(line)

    #
    # Build the output
    #
    displayOutput(terms)

# parseInput(String inputLine) {
def parseInput(inputLine)

    #
    # Validate the input: Must have a single argument of the form MM+NN[+OO...]
    #
    terms = re.match(inputLine, "(\d+){\+(\d+)}+")

    if (terms is None)
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

def displayOutput(terms)
    displayWidth = displayEquation(terms)
    displayCarry(terms, displayWidth)

def displayEquation(terms, maxLength)
    sum = 0

    for term in terms
        sum = sum + term

    sumWidth = len(sum)

    for term in terms
        print term.rjust(sumWidth)

    print "=".rjust(sumWidth, "=")
    print sum
    return sumWidth

def displayCarry(terms, displayWidth)
    print "=".rjust(sumWidth, "=")

    carryString = ""
    #
    # Scan left to right.  The first position that can carry is just to the
    # right of the begining (position 1).
    for position in [1..displayWidth]
        sum = 0
        for term in terms
            sum = sum + term.rjust(sumWidth)[position]

        if sum = 0
            carryString = carryString + " "
        else
            carryString = carryString + sum

    print carryString.rjust(sumWidth)
    
