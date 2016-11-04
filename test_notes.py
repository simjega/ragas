import unittest
import note
import util


def convert_to_notes(list_of_numbers):
    return [note.Note(number) for number in list_of_numbers]


class TestNotes(unittest.TestCase):
    def testArohaFailsWithReverseOrder(self):
        with self.assertRaises(AssertionError):
            util.scale_up(convert_to_notes([3, 2, 1]))
        with self.assertRaises(AssertionError):
            util.scale_up(convert_to_notes([3, 1, 2]))

    def testAvrohaFailsWithNormalOrder(self):
        with self.assertRaises(AssertionError):
            util.scale_down(convert_to_notes([1, 2, 3]))
        with self.assertRaises(AssertionError):
            util.scale_down(convert_to_notes([1, 3, 2]))

    def testNoteListFailsWithNonIterableOrString(self):
        with self.assertRaises(TypeError):
            util.scale_up(1)
        with self.assertRaises(AttributeError):
            util.scale_up("1")
        with self.assertRaises(TypeError):
            util.scale_down(1)
        with self.assertRaises(AttributeError):
            util.scale_down("1")

    def testNoteListSucceeds(self):
        util.scale_up(convert_to_notes([1, 2, 3]))
        util.scale_down(convert_to_notes([3, 2, 1]))
