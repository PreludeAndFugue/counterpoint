import unittest
from counterpoint.counterpoint import (FirstSpecies, Note, HarmonicInterval,
                                       FirstSpeciesError)

b3 = Note('B', octave=3)
c, d, e, f, g, a, b = [Note(name) for name in ('C', 'D', 'E', 'F', 'G', 'A', 'B')]
c5, d5, e5, f5 = [Note(name, octave=5) for name in ('C', 'D', 'E', 'F')]
c5sharp = Note('C', 'sharp', 5)

class TestFirstSpecies(unittest.TestCase):
    def setUp(self):
        """Create two melodic lines."""
        self.cf = [d, f, g, f, e, d]
        self.cm = [d5, a, b, d5, c5sharp, d5]
        self.fs = FirstSpecies(self.cf, self.cm)
        self.fs.check()

    def test_check_all(self):
        self.assertEqual(self.fs.results, [])

    def test_create_intervals(self):
        intervals = [HarmonicInterval(cf, cm) for cf, cm in zip(self.cf, self.cm)]
        self.assertEqual(self.fs.harmonic_intervals, intervals)

    def test_cf_intervals(self):
        """Test that the cantus firmus melodic intervals have been created
        correctly."""
        # TODO

    def test_cm_intervals(self):
        """Test that the counter melody melodic intervals have been created
        correctly."""
        # TODO

    def test_first_interval_correct(self):
        """The first interval must be a unison, fifth or octave."""
        fs = FirstSpecies([c, g, c], [c5, b, c5])
        fs.check()
        self.assertEqual(fs.results, [])

    def test_first_interval_incorrect(self):
        fs = FirstSpecies([c, g, c], [b, b, c5])
        fs.check()
        self.assertEqual(str(fs.results[0]),
                         str(FirstSpeciesError('The counterpoint must begin with a'
                            ' unison, fifth or octave.')))

    def test_last_interval_correct(self):
        # TODO

    def test_last_interval_incorrect(self):
        """The first interval must be a unison, fifth or octave."""
        fs = FirstSpecies([c, g, c], [c5, b, a])
        fs.check()
        self.assertEqual(len(fs.results), 1)
        self.assertEqual(str(fs.results[0]),
                         str(FirstSpeciesError('The counterpoint must end with a'
                            ' unison, fifth or octave.')))

    def test_unisons_correct(self):
        fs = FirstSpecies([c, b3, c], [c, d, c])
        fs.check()
        self.assertEqual(fs.results, [])

    def test_unisons_incorrect(self):
        fs = FirstSpecies([c, d, c], [g, d, g])
        fs.check()
        self.assertEqual(len(fs.results), 1)
        self.assertEqual(str(fs.results[0]),
                         str(FirstSpeciesError('Only the first and last '
                             'intervals may contain a unison')))

    def test_parallel_correct(self):
        fs = FirstSpecies([c, g, c], [c5, b, c5])
        fs.check()
        self.assertEqual(fs.results, [])

    def test_parallel_incorrect(self):
        fs = FirstSpecies([c, d], [c5, d5])
        fs.check()
        self.assertEqual(str(fs.results[0]),
                         str(FirstSpeciesError('Parallel octave or fifth')))


if __name__ == '__main__':
    unittest.main()