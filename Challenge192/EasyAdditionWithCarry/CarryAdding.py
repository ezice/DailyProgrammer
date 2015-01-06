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
    maxLength = getMaxLength(terms)

    # for (int i; i < inputTerms.size(); i++) {
    #     inputTerms[i] = inputTerms[i].padLeft(maxLength)
    # }

>> start here
    for term in terms

    return inputTerms
}

int getMaxLength(String inputTerms[]) {

    #
    # Determine maximum length of the terms.
    #
    for (String term in inputTerms) {
        if (term.length() > maxLength) {
            maxLength = term.length()
        }
    }

    return maxLength
}

displayOutput(String terms[]) {

}
