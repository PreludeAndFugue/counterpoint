import unittest
from counterpoint.counterpoint import HarmonicInterval, Note

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
        self.i2 = HarmonicInterval(self.c4, self.d4)
        self.i2a = HarmonicInterval(self.d4, self.c4)
        self.i2b = HarmonicInterval(self.eflat4, self.d4)
        # Thirds
        self.i3 = HarmonicInterval(self.eflat4, self.c4)
        # Fifths
        self.i5 = HarmonicInterval(self.e4, self.b4)
        self.i5a = HarmonicInterval(self.e4, self.bsharp4)
        # Sixths
        self.i6 = HarmonicInterval(self.eflat4, self.c5)
        # Octaves
        self.i8 = HarmonicInterval(self.c4, self.c5)
        self.i8a = HarmonicInterval(self.c4, self.c5flat)
        # A list of all the intervals
        self.intervals = [self.i2, self.i2a, self.i2b, self.i3, self.i5, self.i5a,
                          self.i6, self.i8, self.i8a]
        
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
        self.assertEqual(self.i3.number, 3)
        self.assertEqual(self.i5a.number, 5)
        self.assertEqual(self.i6.number, 6)
        self.assertEqual(self.i8.number, 8)

    def test_quality(self):
        """Test the quality of an interval."""
        self.assertEqual(self.i2.quality, 'major')
        self.assertEqual(self.i2a.quality, 'major')
        self.assertEqual(self.i2b.quality, 'minor')
        self.assertEqual(self.i3.quality, 'minor')
        self.assertEqual(self.i5.quality, 'perfect')
        self.assertEqual(self.i5a.quality, 'augmented')
        self.assertEqual(self.i8a.quality, 'diminished')
        
    def test_str(self):
        """Test the __str__ method."""
        pass
        
    def test_repr(self):
        """Test the __repr__ method."""
        for interval in self.intervals:
            repr_call = 'Interval(%s, %s)' % (repr(interval.lower_note),
                                              repr(interval.upper_note))
            self.assertEqual(repr(interval), repr_call)
        
        
if __name__ == '__main__':
    unittest.main()