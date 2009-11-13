import unittest
from counterpoint.counterpoint import Interval, Note

class TestInterval(unittest.TestCase):
    def setUp(self):
        """Create notes and intervals to test."""
        self.c4 = Note('C')
        self.csharp4 = Note('C', 'sharp')
        self.d4 = Note('D')
        self.eflat4 = Note('E', 'flat')
        self.e4 = Note('E')
        self.b4 = Note('B')
        self.bsharp4 = Note('B', 'sharp')
        self.c5 = Note('C', 'natural', 5)
        self.c5flat = Note('C', 'flat', 5)
        # Seconds
        self.i2 = Interval(self.c4, self.d4)
        self.i2a = Interval(self.d4, self.c4)
        self.i2b = Interval(self.eflat4, self.d4)
        # Thirds
        self.i3 = Interval(self.eflat4, self.c4)
        # Fifths
        self.i5 = Interval(self.e4, self.b4)
        self.i5a = Interval(self.e4, self.bsharp4)
        # Sixths
        self.i6 = Interval(self.eflat4, self.c5)
        # Octaves
        self.i8 = Interval(self.c4, self.c5)
        self.i8a = Interval(self.c4, self.c5flat)
        
    def test_order_equal(self):
        """Test that the notes in an interval are ordered correctly by
        Interval._order_notes.
        """
        self.assertEqual((self.i2.lower_note, self.i2.upper_note),
                         (self.c4, self.d4))
        self.assertEqual((self.i2a.lower_note, self.i2a.upper_note),
                         (self.c4, self.d4))
        self.assertEqual((self.i8.lower_note, self.i8.upper_note),
                         (self.c4, self.c5))
        self.assertEqual((self.i3.lower_note, self.i3.upper_note),
                          (self.c4, self.eflat4))
                          
    def test_order_not_equal(self):
        self.assertNotEqual((self.i2.lower_note, self.i2.upper_note),
                            (self.d4, self.c4))
                         
    def test_number(self):
        """Test the number of an interval."""
        self.assertEqual(self.i2.number, 2)
        self.assertEqual(self.i2a.number, 2)
        self.assertEqual(self.i2b.number, 2)
        self.assertEqual(self.i5a.number, 5)
        self.assertEqual(self.i6.number, 6)
        self.assertEqual(self.i8.number, 8)

    def test_quality(self):
        """Test the quality of an interval."""
        self.assertEqual(self.i2.quality, 'major')
        self.assertEqual(self.i2a.quality, 'major')
        self.assertEqual(self.i2b.quality, 'minor')
        self.assertEqual(self.i5.quality, 'perfect')
        self.assertEqual(self.i5a.quality, 'augmented')
        self.assertEqual(self.i8a.quality, 'diminished')
        
if __name__ == '__main__':
    unittest.main()