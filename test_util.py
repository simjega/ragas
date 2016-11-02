import unittest
import note
import util


class TestNotes(unittest.TestCase):
    def testArohaFailsWithReverseOrder(self):
        self.assertEqual("'N", util.convert_note_to_name(note.Note(11, -1)))
