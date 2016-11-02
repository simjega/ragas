
class NoteList(object):
    def __init__(self, notes, validation=lambda x: True):
        assert validation(notes)
        self.notes = notes

    def __repr__(self):
        return self.notes.__repr__()
