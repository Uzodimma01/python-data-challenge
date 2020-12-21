'''This program reads the name of a note from the user and displays the note's frequency.'''

# Read the name of the note from the user
note = str(input("Please enter the key note you wish to know the frequency: ")).upper()

# Slice the note variable
alpha = note[0]
num = int(note[1]) # Type cast the num string to integer

if note in ("D4","E4","F4","G4","A4","B4"):

    # Store the notes in a dictionary
    notes = {"D4":"293.66","E4":"329.63","F4":"349.23","G4":"392.00","A4":"440.00","B4":"493.88"}

    # Get the value of the key entered by the user
    freq = notes[note]

    # Display the frequency of the note
    print("The frequency of note {0} is {1}Hz".format(note,freq))


elif note[0] == "C"  and num >= 0 and num <= 8:

    # Compute the frequency of the note
    freq = 261.63/(2**(4-num))

    # Display the frequency of the note
    print("The frequency of note {0} is {1:.2f}Hz".format(note,freq))
else:
    print("You entered an invalid note")