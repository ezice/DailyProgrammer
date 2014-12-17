
while (!eof()) {
    #
    # Parse the input
    #
    terms = parseInput(readln())

    #
    # Build the output
    #
    displayOutput(terms)
}

parseInput(String inputLine) {
#
# Validate the input: Must have a single argument of the form MM+NN[+OO...]
#
    if (intpuLine.match("\d+{\+\d+}+))") {
        usage()
        exit()
    }

#
# Pad the terms on the left (right-justify).
#
    String inputTerms[] = inputLine.split("+")
    int maxLength = getMaxLength(inputTerms)

    for (int i; i < inputTerms.size(); i++) {
        inputTerms[i] = inputTerms[i].padLeft(maxLength)
    }

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
