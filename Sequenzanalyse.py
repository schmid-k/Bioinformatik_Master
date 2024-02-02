startingSequence = "atgctgtcgctatttcg"

upSequence = startingSequence.upper()

compSequence = ""

inverted = ""


def correctSequence(sequence):
    """Checks if a given sequence uses the right syntax and changes it to upper letters if not already done"""
    sequence = sequence.upper()
    for character in sequence:
        if character not in "ATCG":
            print("Sequence is not correct")
            break
    print("Sequence is correct")

def complementSequence(sequence):
    """Creates the complementary sequence to a given sequence"""
    global compSequence
    sequence = sequence.upper()
    for char in sequence:
        if char == "A":
            compSequence += "T"
        elif char == "T":
            compSequence += "A"
        elif char == "C":
            compSequence += "G"
        elif char == "G":
            compSequence += "C"
    return compSequence


def invertSequence(sequence):
    """Inverts a given sequence from 3'-5' to 5'-3' and vice versa"""
    global inverted
    inverted = sequence[::-1]
    return inverted


def nucleotides(sequence):
    """Calculates the percentage of the nucleotides in a given sequence"""
    length = len(sequence)
    adenine = sequence.count("A")
    print(f"Adenine: {round(adenine / length * 100, 1)}%")
    thymine = sequence.count("T")
    print(f"Thymine: {round(thymine / length * 100, 1)}%")
    guanine = sequence.count("G")
    print(f"Guanine: {round(guanine / length * 100, 1)}%")
    cytosine = sequence.count("C")
    print(f"Cytosine: {round(cytosine / length * 100, 1)}%")
    return ""



correctSequence(startingSequence)
complementSequence(startingSequence)
invertSequence(compSequence)

print(upSequence)
print(compSequence)
print(inverted)
print(nucleotides(upSequence))
