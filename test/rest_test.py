import unittest
from music.music import Rest

class TestRestCreation(unittest.TestCase):
    def setUp(self):
        self.r16 = Rest(16)
        self.r32 = Rest(32)
        self.r1 = Rest(1)
        
    def test_repr_16(self):
        self.assertEqual(repr(self.r16), 'Rest(16)')
        
    def test_repr_32(self):
        self.assertEqual(repr(self.r32), 'Rest(32)')
        
    def test_repr_1(self):
        self.assertEqual(repr(self.r1), 'Rest(1)')
        
    def test_str_16(self):
        self.assertEqual(str(self.r16), 'crotchet rest')
    
    def test_str_32(self):
        self.assertEqual(str(self.r32), 'minim rest')
        
    def test_str_11(self):
        self.assertEqual(str(self.r1), 'hemi-demi-semiquaver rest')
        
    def test_duration_16(self):
        self.assertEqual(self.r16.duration, 16)
        
    def test_duration_32(self):
        self.assertEqual(self.r32.duration, 32)
        
    def test_duration_11(self):
        self.assertEqual(self.r1.duration, 1)
        
if __name__ == '__main__':
    unittest.main()