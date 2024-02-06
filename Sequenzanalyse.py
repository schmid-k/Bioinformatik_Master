import re
import tkinter as tk

from tkinter import simpledialog

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


# Eine Tkinter-Anwendung erstellen
root = tk.Tk()
# Das Fenster sofort wieder ausblenden, da wir nur das Dialogfeld anzeigen möchten
root.withdraw()

# Ein Dialogfeld anzeigen und die Eingabe des Benutzers in einer Variablen speichern
startingSequence = simpledialog.askstring(title="Sequenzeingabe", prompt="Bitte geben Sie Ihre Sequenz ein:")


# Ein Tkinter-Fenster erstellen
window = tk.Tk()

# Zwei Buttons erstellen
button1 = tk.Button(window, text="Complementary Sequence", command=complementSequence)
button2 = tk.Button(window, text="Inverted Sequence", command=invertSequence)
button3 = tk.Button(window, text="Reverse-Complement Sequence", command=reverseComplement)
button4 = tk.Button(window, text="Nucleotides Percentage", command=nucleotides)

# Die Buttons zum Fenster hinzufügen
button1.pack()
button2.pack()
button3.pack()
button4.pack()

# Das Fenster anzeigen
window.mainloop()

print()