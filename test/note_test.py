import unittest
from music.music import Note

class TestNoteCreation(unittest.TestCase):
    def setUp(self):
        self.c = Note('C')
        self.dsharp = Note('D', 'sharp', 5, 2)
        self.eflat = Note('E', 'flat', 3, 8)
        
    def test_str(self):
        self.assertEqual(str(self.c), 'C')
        self.assertEqual(str(self.dsharp), 'D#')
        self.assertEqual(str(self.eflat), 'Eb')
        
    def test_repr(self):
        pass
        
    def test_octave(self):
        self.assertEqual(self.c.octave, 4)
        self.assertEqual(self.dsharp.octave, 5)
        self.assertEqual(self.eflat.octave, 3)
        
    def test_duration(self):
        self.assertEqual(self.c.duration, 16)
        self.assertEqual(self.dsharp.duration, 2)
        self.assertEqual(self.eflat.duration, 8)
        
if __name__ == '__main__':
    unittest.main()