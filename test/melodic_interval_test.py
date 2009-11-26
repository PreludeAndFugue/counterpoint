import unittest
from counterpoint.counterpoint import MelodicInterval, Note

class MelodicTest(unittest.TestCase):
    def setUp(self):
        self.c4 = Note('C')
        self.d4 = Note('D')
        self.c5 = Note('C', octave = 5)
        # up intervals
        self.u1 = MelodicInterval(self.c4, self.d4)
        self.u2 = MelodicInterval(self.c4, self.c5)
        self.u3 = MelodicInterval(self.d4, self.c5)
        # down intervals
        self.d1 = MelodicInterval(self.d4, self.c4)
        self.d2 = MelodicInterval(self.c5, self.d4)
        self.d3 = MelodicInterval(self.c5, self.c4)
        # level intervals
        self.l1 = MelodicInterval(self.c4, self.c4)
        self.l2 = MelodicInterval(self.d4, self.d4)
        self.l3 = MelodicInterval(self.c5, self.c5)
        self.intervals = [self.u1, self.u2, self.u3, self.d1, self.d2, self.d3,
                          self.l1, self.l2, self.l3]

    def test_up(self):
        """Test ascending intervals."""
        for interval in (self.u1, self.u2, self.u3):
            self.assertEqual(interval.direction, 'u')
            self.assertEqual(interval.directions[interval.direction], 'ascending')

    def test_down(self):
        """Test descending intervals."""
        for interval in (self.d1, self.d2, self.d3):
            self.assertEqual(interval.direction, 'd')
            self.assertEqual(interval.directions[interval.direction], 'descending')

    def test_level(self):
        """Test level intervals."""
        for interval in (self.l1, self.l2, self.l3):
            self.assertEqual(interval.direction, 'l')
            self.assertEqual(interval.directions[interval.direction], 'level')

    def test_str(self):
        pass

    def test_repr(self):
        """Test the __repr__ method."""
        for interval in self.intervals:
            repr_call = 'MelodicInterval(%s, %s)' % (repr(interval.first_note),
                                                     repr(interval.second_note))
            self.assertEqual(repr(interval), repr_call)


if __name__ == '__main__':
    unittest.main()