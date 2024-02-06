import re

startingSequence = "AGGTCGGTTG"
correctedSequence = ""
compSequence = ""
inverted = ""


def correctSequence():
    """Checks if a given sequence uses the right syntax and changes it to upper letters if not already done"""
    sequence = startingSequence
    upSequence = sequence.upper()
    global correctedSequence
    correctedSequence = re.sub("[0-9 \n]", "", upSequence)
    for character in correctedSequence:
        if character not in "ATCG":
            return print("Sequence is not correct")
    print("The corrected sequence is:", correctedSequence)
    return correctedSequence

def complementSequence(sequence):
    """Creates the complementary sequence to a given sequence"""
    global compSequence
    sequence = correctedSequence
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

def invertSequence():
    """Inverts a given sequence from 3'-5' to 5'-3' and vice versa"""
    global inverted
    sequence = correctedSequence
    inverted = sequence[::-1]
    return inverted

def nucleotides():
    """Calculates the percentage of the nucleotides in a given sequence"""
    sequence = startingSequence
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

def reverseComplement():
    complementSequence()
    invertSequence()
    return ""


correctSequence()

