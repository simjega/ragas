import util


class Note(object):
    def __init__(self, sulfege, octave=0):
        self.sulfege = sulfege
        self.octave = octave

    def __repr__(self):
        return util.convert_note_to_name(self)
