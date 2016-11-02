# Current definitions:
# Prerequisite: Assume all definitions are relative to some key note, F
# Sulfege: The relative chromatic scale off of F
#    For now its 1 of 12 possible notes
# Octave: A power of 2 multiple of F: F * 2 ^ N (N is any integer)
#    For now its described by the power of 2: N
# Note: A tuple of Sulfege and Octave
#


TOTAL_NOTES_IN_OCTAVE = 12
SOLFEGE_NUMBERS = list(range(TOTAL_NOTES_IN_OCTAVE))
SOLFEGE_NAMES = ["S", "r", "R", "g", "G", "m", "M", "P", "d", "D", "n", "N"]
NUMBER_TO_NAME = dict(zip(SOLFEGE_NUMBERS, SOLFEGE_NAMES))
NAME_TO_NUMBER = dict(zip(SOLFEGE_NAMES, SOLFEGE_NUMBERS))
OCTAVE_MODIFIER = "'"

NAME_TO_NUMBER["s"] = 0