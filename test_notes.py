import unittest
import note
import util


def convert_to_notes(list_of_numbers):
    return [note.Note(number) for number in list_of_numbers]


class TestNotes(unittest.TestCase):
    def testArohaFailsWithReverseOrder(self):
        with self.assertRaises(AssertionError):
            util.aroha(convert_to_notes([3, 2, 1]))
        with self.assertRaises(AssertionError):
            util.aroha(convert_to_notes([3, 1, 2]))

    def testAvrohaFailsWithNormalOrder(self):
        with self.assertRaises(AssertionError):
            util.avroha(convert_to_notes([1, 2, 3]))
        with self.assertRaises(AssertionError):
            util.avroha(convert_to_notes([1, 3, 2]))

    def testNoteListFailsWithNonIterableOrString(self):
        with self.assertRaises(TypeError):
            util.aroha(1)
        with self.assertRaises(AttributeError):
            util.aroha("1")
        with self.assertRaises(TypeError):
            util.avroha(1)
        with self.assertRaises(AttributeError):
            util.avroha("1")

    def testNoteListSucceeds(self):
        util.aroha(convert_to_notes([1, 2, 3]))
        util.avroha(convert_to_notes([3, 2, 1]))
