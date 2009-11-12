import unittest
from counterpoint.counterpoint import Interval, Note

class TestInterval(unittest.TestCase):
    def setUp(self):
        """Create notes to test intervals."""
        self.c4 = Note('C')
        self.csharp4 = Note('C', 'sharp')
        self.d4 = Note('D')
        self.eflat4 = Note('E', 'flat')
        self.c5 = Note('C', 'natural', 5)
        
        self.i1 = Interval(self.c4, self.d4)
        self.i1a = Interval(self.d4, self.c4)
        self.i2 = Interval(self.c4, self.c5)
        self.i3 = Interval(self.eflat4, self.d4)
        
    def test_order_equal(self):
        """Test that the notes in an interval are ordered correctly by
        Interval._order_notes.
        """
        self.assertEqual((self.i1.lower_note, self.i1.upper_note),
                         (self.c4, self.d4))
        self.assertEqual((self.i1a.lower_note, self.i1a.upper_note),
                         (self.c4, self.d4))
        self.assertEqual((self.i2.lower_note, self.i2.upper_note),
                         (self.c4, self.c5))
        self.assertEqual((self.i3.lower_note, self.i3.upper_note),
                          (self.d4, self.eflat4))
                          
    def test_order_not_equal(self):
        self.assertNotEqual((self.i1.lower_note, self.i1.upper_note),
                            (self.d4, self.c4))
                         
    def test_number(self):
        """Test the number of an interval."""
        self.assertEqual(self.i1.number, 2)
        self.assertEqual(self.i1a.number, 2)
        self.assertEqual(self.i2.number, 8)
        self.assertEqual(self.i3.number, 2)


        
if __name__ == '__main__':
    unittest.main()