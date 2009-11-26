# TODO: the durations need to be changed to take account of triplets.
# Multiplying all durations by three should work. So crotchet = 48.
DURATION_NAMES = {1: 'hemi-demi-semiquaver',
                  2: 'demi-semiquaver',
                  4: 'semiquaver',
                  8: 'quaver',
                  12: 'dotted quaver',
                  16: 'crotchet',
                  24: 'dotted crotchet',
                  32: 'minim',
                  48: 'dotted minim',
                  64: 'semibreve',
                  128: 'breve'}

class FirstSpeciesError(Exception):
    """Base class for all errors dedected by the First Species checker."""
    pass


class FirstSpecies(object):
    """Check the correctness of first species counterpoint."""
    def __init__(self, cantus_firmus, counter_melody):
        self.cantus_firmus = cantus_firmus
        self.counter_melody = counter_melody
        self.harmonic_intervals = self._create_harmonic_intervals()
        self.results = []

    def _create_harmonic_intervals(self):
        """Return a list of HarmonicInterval objects by comparing the cantus firmus
        with the counter melody."""
        return [HarmonicInterval(note_cf, note_cm) for note_cf, note_cm
                        in zip(self.cantus_firmus, self.counter_melody)]

    def _create_melodic_intervals(self, melody):
        """Return a list of MelodicInterval objects from the given melody which
        is a list of Note objects."""
        return [MelodicInterval(n1, n2) for n1, n2 in zip(melody[:-1], melody[1:])]

    def check(self):
        """The main method for checking the first species counterpoint.

        This method calls all the '_rule_*' methods saving the results in """
        rules = [self._rule_first_last_interval,
                 self._rule_unisons,
                 self._rule_parallel_movement, 
                 self._rule_hidden_parallel]
        for rule in rules:
            rule()

    def _rule_first_last_interval(self):
        """The first and last intervals should only be a unison, fifth or
        octave.
        """
        correct_intervals = (1, 5, 8)
        if self.harmonic_intervals[0].number not in correct_intervals:
            self.results.append(FirstSpeciesError('The counterpoint must begin '
                'with a unison, fifth or octave.'))
        if self.harmonic_intervals[-1].number not in correct_intervals:
            self.results.append(FirstSpeciesError('The counterpoint must end '
                'with a unison, fifth or octave.'))

    def _rule_unisons(self):
        """Only the first and last intervals may be unisons."""
        intervals = self.harmonic_intervals[1:-1]
        for interval in intervals:
            if interval.number == 1:
                self.results.append(FirstSpeciesError('Only the first and last '
                    'intervals may contain a unison'))

    def _rule_parallel_movement(self):
        """Avoid parallel fifths or octaves between any two parts."""
        interval_pairs = [(int1.number, int2.number) for int1, int2 in
                zip(self.harmonic_intervals[:-1], self.harmonic_intervals[1:])]
        forbidden_intervals = (1, 5, 8, 12, 15, 19, 23, 27)
        for int1, int2 in interval_pairs:
            if int1 == int2 and int1 in forbidden_intervals:
                self.results.append(FirstSpeciesError('Parallel octave or '
                    'fifth'))

    def _rule_hidden_parallel(self):
        """Avoid 'hidden' parallel fifths or octaves: that is, movement by
        similar motion to a perfect fifth or octave, unless one part
        (sometimes restricted to the higher of the parts) moves by step."""
        pass

    def pretty(self):
        """A prettified string of the counterpoint."""
        return [str(i) for i in self.harmonic_intervals]

    def print_results(self):
        """Print the results."""
        pass


class Rest(object):
    """A musical rest."""

    def __init__(self, duration=4):
        self.duration = duration

    def __repr__(self):
        return "Rest(%s)" % self.duration

    def __str__(self):
        return DURATION_NAMES[self.duration] + ' rest'


class Note(object):
    """A musical note.

    Use the scientific pitch notation where middle c is C4:
    http://en.wikipedia.org/wiki/Scientific_pitch_notation
    """

    name_number = {'C': 0, 'D': 2, 'E': 4, 'F': 5,
                     'G': 7, 'A': 9, 'B': 11}
    acc_number = {'natural': 0, 'sharp': 1, 'flat': -1}
    acc_print = {'natural': '', 'flat': 'b', 'sharp': '#'}

    def __init__(self, name='C', accidental='natural', octave=4, duration=16):
        self.name = name
        self.accidental = accidental
        self.octave = octave
        self.duration = duration
        self.midi_number = self._midi_number()

    def _midi_number(self):
        """Return an integer which represents the MIDI number of the note.
        http://en.wikipedia.org/wiki/Note#Note_designation_in_accordance_with_octave_name
        """
        return (12*(self.octave + 1)
                + Note.name_number[self.name]
                + Note.acc_number[self.accidental])

    def add_interval(self, interval=5):
        """Return a new Note object created from the current note with the added
        interval."""
        pass

    def __str__(self):
        return ''.join((self.name, str(self.octave), Note.acc_print[self.accidental]))

    def __repr__(self):
        return 'Note("%s", "%s", %s, %s)' % (
            self.name, self.accidental, self.octave, self.duration)

    def __eq__(self, other_note):
        """Two notes are identical if their attributes are identical."""
        return (self.name, self.accidental, self.octave, self.duration) == (
                other_note.name, other_note.accidental, other_note.octave,
                other_note.duration)


class Interval(object):
    """A musical interval.
    """
    name_number = {'C': 1, 'D': 2, 'E': 3, 'F': 4,
                     'G': 5, 'A': 6, 'B': 7}
    acc_add = {'natural': 0, 'sharp': 1, 'flat': -1}
    qualities = {1: {-1: 'diminished', 0: 'perfect', 1: 'augmented'},
                 2: {0: 'diminished', 1: 'minor', 2: 'major', 3: 'augmented'},
                 3: {3: 'minor', 4: 'major'},
                 4: {4: 'diminished', 5: 'perfect', 6: 'augmented'},
                 5: {6: 'diminished', 7: 'perfect', 8: 'augmented'},
                 6: {8: 'minor', 9: 'major', 10: 'augmented'},
                 7: {10: 'minor', 11: 'major'}}

    def __init__(self, note1, note2):
        self.number = self._number(note1, note2)
        self.quality = self._quality(note1, note2)

    def __eq__(self, other):
        """Testing the equality of two intervals."""
        return (self.lower_note, self.upper_note, self.number, self.quality) == (
                other.lower_note, other.upper_note, other.number, other.quality)

    def _order_notes(self, note1, note2):
        """Return the notes in order with the lowest note first."""
        if note1.midi_number <= note2.midi_number:
            return note1, note2
        else:
            return note2, note1

    def _number(self, note1, note2):
        """Calculate the interval number.

        http://en.wikipedia.org/wiki/Interval_%28music%29#Number
        """
        lower, higher = self._order_notes(note1, note2)
        octave_diff = higher.octave - lower.octave
        scale_diff = (self.name_number[higher.name]
                      - self.name_number[lower.name])
        return scale_diff + 7*octave_diff + 1

    def _quality(self, note1, note2):
        """Calculate the quality of the interval.

        http://en.wikipedia.org/wiki/Interval_%28music%29#Quality
        """
        lower, higher = self._order_notes(note1, note2)
        key_1 = self.number % 7
        key_1 = key_1 if key_1 else 7
        key_2 = (higher.midi_number - lower.midi_number) % 12
        if (key_1, key_2) == (1, 11):
            # this is a hack to account for diminished octaves, fifteenths, etc.
            key_2 = -1
        return self.qualities[key_1][key_2]

    def invert(self, direction='up'):
        """Invert the interval."""
        raise NotImplemented

class HarmonicInterval(Interval):
    """A harmonic interval is created by playing two notes simultaneously."""
    def __init__(self, note1, note2):
        super(HarmonicInterval, self).__init__(note1, note2)
        self.lower_note, self.upper_note = self._order_notes(note1, note2)

    def __str__(self):
        return '%s %s between %s and %s' % (self.quality,
                                            card_to_ord(self.number),
                                            str(self.lower_note),
                                            str(self.upper_note))

    def __repr__(self):
        return 'HarmonicInterval(%s, %s)' % (repr(self.lower_note),
                                             repr(self.upper_note))


class MelodicInterval(Interval):

    directions = {'u': 'ascending', 'd': 'descending', 'l': 'level'}

    """A melodic interval is created when two notes are played consecutively."""
    def __init__(self, note1, note2):
        super(MelodicInterval, self).__init__(note1, note2)
        self.first_note = note1
        self.second_note = note2
        self.direction = self._direction(note1, note2)

    def _direction(self, note1, note2):
        """Calculate the direction of the interval. Used for melodic intervals.

        If the second note is higher than the first, then the direction is 'u'.
        If the second note is lower, then 'd'.
        Otherwise 'l' (for level)
        """
        if note1.midi_number > note2.midi_number:
            return 'd'
        if note1.midi_number < note2.midi_number:
            return 'u'
        return 'l'

    def __str__(self):
        return '%s %s %s between %s and %s' % (self.directions[self.direction],
                                               self.quality,
                                               card_to_ord(self.number),
                                               str(self.first_note),
                                               str(self.second_note))

    def __repr__(self):
        return 'MelodicInterval(%s, %s)' % (repr(self.first_note),
                                             repr(self.second_note))

# some helper functions
def card_to_ord(n):
    """Return a string which will turn a cardinal number (integer) into an
    ordinal number.

    >>> card_to_ord(10)
    10th
    >>> card_to_ord(1)
    1st
    >>> card_to_ord(2)
    2nd
    >>> card_to_ord(12)
    12th
    >>> card_to_ord(55)
    55th
    """
    final_digit = n%10
    ending = {1: 'st', 2: 'nd', 3: 'rd'}
    if final_digit in (1, 2, 3) and n%100 not in (11, 12, 13):
        return '%s%s' % (n, ending[final_digit])
    return '%sth' % n

def main():
    n1 = Note('F', 5)
    n2 = Note('C')
    print interval(n1, n2)

if __name__ == '__main__':
    main()