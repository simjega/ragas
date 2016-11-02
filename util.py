import config
from note_list import NoteList
import note


def note_metric(note):
    return note.sulfege + config.TOTAL_NOTES_IN_OCTAVE * note.octave


def convert_int_to_note(integer):
    return note.Note(integer)


def convert_name_to_note(name):
    name = str(name)
    length = len(name)

    if length == 1:
        letter = name[0]
        octave = 0
    elif name[0] is config.OCTAVE_MODIFIER:
        letter = name[-1]
        octave = - (length - 1)
    else:
        letter = name[0]
        octave = length - 1

    return note.Note(config.NAME_TO_NUMBER[letter], octave=octave)


def convert_note_to_name(nte):
    letter = config.NUMBER_TO_NAME[nte.sulfege]
    octave = nte.octave

    return letter + octave * "'" if octave > 0 else -octave * "'" + letter


def aroha(notes):
    return NoteList(notes, lambda notes: sorted(notes, key=note_metric) == notes)


def avroha(notes):
    return NoteList(notes, lambda notes: sorted(notes, key=note_metric, reverse=True) == notes)
