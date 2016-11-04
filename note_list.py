
class NoteList(object):
    def __init__(self, notes, validation=lambda x: True):
        assert validation(notes)
        self.notes = notes

    def __repr__(self):
        return " ".join([note.__repr__() for note in self.notes])
