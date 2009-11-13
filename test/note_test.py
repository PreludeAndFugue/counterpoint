import unittest
from counterpoint.counterpoint import Note

class TestNoteCreation(unittest.TestCase):
    def setUp(self):
        note_args = [
            (('C'), ('C4', 'C', 'natural', 4, 16, 60)),
            (('D', 'sharp', 5, 2), ('D5#', 'D', 'sharp', 5, 2, 75)),
            (('E', 'flat', 3, 8), ('E3b', 'E', 'flat', 3, 8, 51)),
            (('F', 'natural', 6, 16), ('F6', 'F', 'natural', 6, 16, 89)),
            (('G', 'sharp', 2, 32), ('G2#', 'G', 'sharp', 2, 32, 44)),
            (('A', 'flat', 1, 64), ('A1b', 'A', 'flat', 1, 64, 32)),
            (('B', 'natural', 4, 64), ('B4', 'B', 'natural', 4, 64, 71))
        ]
        self.notes = [(Note(*args), results) for args, results in note_args]
        
    def test_str(self):
        """Test the result of calling __str__."""
        for note, results in self.notes:
            self.assertEqual(str(note), results[0])
            
    def test_name(self):
        """Test the result of calling Note.name."""
        for note, results in self.notes:
            self.assertEqual(note.name, results[1])
            
    def test_accidental(self):
        """Test the result of calling Note.accidental."""
        for note, results in self.notes:
            self.assertEqual(note.accidental, results[2])
        
    def test_octave(self):
        """Test the result of calling Note.octave."""
        for note, results in self.notes:
            self.assertEqual(note.octave, results[3])
        
    def test_duration(self):
        """Test the result of calling Note.duration."""
        for note, results in self.notes:
            self.assertEqual(note.duration, results[4])
            
    def test_midi_number(self):
        """Test the result of calling Note.midi_number."""
        for note, results in self.notes:
            self.assertEqual(note.midi_number, results[5])
            
    def test_repr(self):
        """Test the result of calling __repr__."""
        for note, results in self.notes:
            note_repr = 'Note("%s", "%s", %s, %s)' % results[1:-1]
            self.assertEqual(repr(note), note_repr)
        
if __name__ == '__main__':
    unittest.main()
