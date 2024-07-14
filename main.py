from random import randint

# Define music variables that will be used
notes : list = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
chord_tonality : list = ["", "m", "sus2", "sus4", "5", "6"]
chord_extensions : list = ["7", "maj7" "9", "b9", "#9", "11", "b11", "#11", "13", "b13", "#13"]

# Define desired functions

# Random rhythm generator

def rand_rhythm(grouping:int=4):
    rhythm : list = [bool(randint(0, 1)) for n in range(grouping)]
    return rhythm

# Random melody selector

def rand_melody(length:int=4, scale:list=notes):
    melody : list = [scale[randint(0, (len(scale) - 1))] for n in range(length)]
    return melody

# Random Scale builder
def rand_scale_builder(length:int=7):
    temp_notes : list = notes
    scale: list = []
    for n in range(length):
        degree : int = randint(0, (len(temp_notes)-1))
        scale.append(temp_notes[degree])
        temp_notes.pop(degree)
    return sorted(scale)