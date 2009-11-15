import unittest
from counterpoint.counterpoint import (FirstSpecies, Note, Interval,
                                       FirstSpeciesError)

c, d, e, f, g, a, b = [Note(name) for name in ('C', 'D', 'E', 'F', 'G', 'A', 'B')]
c5, d5, e5, f5 = [Note(name, octave=5) for name in ('C', 'D', 'E', 'F')]
c5sharp = Note('C', 'sharp', 5)

class TestFirstSpecies(unittest.TestCase):
    def setUp(self):
        """Create two melodic lines."""
        self.cf = [d, f, g, f, e, d]
        self.cm = [d5, a, b, d5, c5sharp, d5]
        
    def test_create_intervals(self):
        intervals = [Interval(cf, cm) for cf, cm in zip(self.cf, self.cm)]
        fs = FirstSpecies(self.cf, self.cm)
        self.assertEqual(fs.intervals, intervals)
        
    def test_first_interval_correct(self):
        """The first interval must be a unison, fifth or octave."""
        fs1 = FirstSpecies([c, g, c], [c5, b, c5])
        fs1.check()
        self.assertEqual(fs1.results, [])
        
    def test_first_interval_incorrect(self):
        fs2 = FirstSpecies([c, g, c], [b, b, c5])
        fs2.check()
        self.assertEqual(str(fs2.results[0]),
                         str(FirstSpeciesError('The counterpoint must begin with a'
                            ' unison, fifth or octave.')))
                            
    def test_last_interval_incorrect(self):
        fs2 = FirstSpecies([c, g, c], [c5, b, a])
        fs2.check()
        self.assertEqual(str(fs2.results[0]),
                         str(FirstSpeciesError('The counterpoint must end with a'
                            ' unison, fifth or octave.')))
        
if __name__ == '__main__':
    unittest.main()