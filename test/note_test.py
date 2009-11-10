import unittest
from music.music import Note

class TestNoteCreation(unittest.TestCase):
    def setUp(self):
        self.c = Note('C')
        self.dsharp = Note('D', 'sharp', 5, 2)
        self.eflat = Note('E', 'flat', 3, 8)
        
    def test_str_c(self):
        self.assertEqual(str(self.c), 'C')
        
    def test_str_d(self):
        self.assertEqual(str(self.dsharp), 'D#')
        
    def test_str_e(self):
        self.assertEqual(str(self.eflat), 'Eb')
        
    def test_repr(self):
        pass
        
    def test_octave_c(self):
        self.assertEqual(self.c.octave, 4)
    
    def test_octave_d(self):
        self.assertEqual(self.dsharp.octave, 5)
        
    def test_octave_e(self):
        self.assertEqual(self.eflat.octave, 3)
        
    def test_duration_c(self):
        self.assertEqual(self.c.duration, 16)
        
    def test_duration_d(self):
        self.assertEqual(self.dsharp.duration, 2)
        
    def test_duration_e(self):
        self.assertEqual(self.eflat.duration, 8)
        
if __name__ == '__main__':
    unittest.main()