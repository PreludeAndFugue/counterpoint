import unittest
from counterpoint.counterpoint import Rest

class TestRestCreation(unittest.TestCase):
    def setUp(self):
        self.test_cases = ((1, 'Rest(1)', 'hemi-demi-semiquaver rest'),
                           (2, 'Rest(2)', 'demi-semiquaver rest'),
                           (4, 'Rest(4)', 'semiquaver rest'),
                           (8, 'Rest(8)', 'quaver rest'),
                           (16, 'Rest(16)', 'crotchet rest'))
        
    def test_repr(self):
        """Test the result of calling __repr__"""
        for duration, repr_, _ in self.test_cases:
            self.assertEqual(repr(Rest(duration)), repr_)
        
    def test_str(self):
        """Test the result of calling __str__"""
        for duration, _, str_ in self.test_cases:
            self.assertEqual(str(Rest(duration)), str_)
        
    def test_duration(self):
        """Test the result of calling Rest.duration."""
        for duration_, _, _ in self.test_cases:
            self.assertEqual(Rest(duration_).duration, duration_)
        
if __name__ == '__main__':
    unittest.main()