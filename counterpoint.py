import math

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
                  
class FirstSpecies(object):
    """Check the correctness of some first species counterpoint."""
    def __init__(self):
        self.cantus_firmus = None
        self.counter_melody = None
        self.intervals = None
        self.results = None
        
    def _create_intervals(self):
        """Create a list of interval objects by comparing the cantus firmus
        with the counter melody."""
        self.interval = [Interval(note_cf, note_cm) for note_cf, note_cm
                        in zip(self.cantus_firmus, self.counter_melody)]
                        
    def check(self):
        """The main method for checking the first species counterpoint."""
        pass
        
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
                + self.name_number[self.name]
                + self.acc_number[self.accidental])
        
    def add_interval(self, interval=5):
        pass
        
    def __str__(self):
        return ''.join((self.name, str(self.octave), self.acc_print[self.accidental]))
        
    def __repr__(self):
        return 'Note("%s", "%s", %s, %s)' % (
            self.name, self.accidental, self.octave, self.duration)


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
        self.lower_note, self.upper_note = self._order_notes(note1, note2)
        self.number = self._number()
        self.quality = self._quality()
        
    def __str__(self):
        return '%s %s' % (self.quality, card_to_ord(self.number))
        
    def __repr__(self):
        pass
        
    def _order_notes(self, note1, note2):
        """Return the notes in order with the lowest note first."""
        if note1.midi_number <= note2.midi_number:
            return note1, note2
        else:
            return note2, note1
        
    def _number(self):
        """Calculate the interval number."""
        octave_diff = self.upper_note.octave - self.lower_note.octave
        scale_diff = (self.name_number[self.upper_note.name]
                      - self.name_number[self.lower_note.name])
        return scale_diff + 7*octave_diff + 1
        
    def _quality(self):
        """Calculate the quality of the interval."""
        key_1 = self.number % 7
        key_1 = key_1 if key_1 else 7
        key_2 = (self.upper_note.midi_number - self.lower_note.midi_number) % 12
        #print 'key_1', key_1
        if (key_1, key_2) == (1, 11):
            # this is a hack to account for diminished octaves, fifteenths, etc.
            key_2 = -1
        return self.qualities[key_1][key_2]
        
    def invert(self, direction='up'):
        """Invert the interval."""
        raise NotImplemented

# some helper functions
def card_to_ord(n):
    """Return a string which will turn a cardinal number into an ordinal number.
    
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
    if final_digit in (1, 2, 3):
        if n%100 in (11, 12, 13):
            return str(n) + 'th'
        else:
            ending = {1: 'st', 2: 'nd', 3: 'rd'}
            return str(n) + ending[final_digit]
    else:
        return str(n) + 'th'

def main():
    n1 = Note('F', 5)
    n2 = Note('C')
    print interval(n1, n2)
    
if __name__ == '__main__':
    main()