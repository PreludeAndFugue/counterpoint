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
    """
    
    acc = {'natural': '', 'flat': 'b', 'sharp': '#'}
    
    def __init__(self, name='C', accidental='natural', octave=4, duration=16):
        self.name = name
        self.accidental = accidental
        self.octave = octave
        self.duration = duration
        
    def add_interval(self, interval=5):
        pass
        
    def __str__(self):
        return ''.join((self.name, self.acc[self.accidental]))
        
    def __repr__(self):
        return 'Note("%s", "%s", %s, %s)' % (
            self.name, self.accidental, self.octave, self.duration)


class Interval(object):
    """A musical interval."""
    def __init__(self, note1, note2):
        self.lower_note, self.upper_note = self._order_notes(note1, note2)
        self.number = self._number()
        self.quality = self._quality()
        
    def _order_notes(self, note1, note2):
        """Return the notes in order with the lowest note first."""
        if self._note_position(note1) <= self._note_position(note2):
            return note1, note2
        else:
            return note2, note1
        
    def _note_position(self, note):
        """Return an integer representing the absolute position of the note.
        
        For internal purposes only - the implementation may change. However,
        the relative position of two notes should always be equal.
        """
        name_position = {'C': 1, 'D': 3, 'E': 5, 'F': 6,
                         'G': 8, 'A': '10', 'B': 12}
        acc_add = {'natural': 0, 'sharp' 1, 'flat': -1}
        return name_position[note.name] + 7*note.octave + acc_add[note.accidental]
        
    def _number(self):
        """Calculate the interval number."""
        octave_diff = self.upper_note.octave - self.lower_note.octave
        scale_diff = ord(self.upper_note.name) - ord(sef.lower_note.name)
        return scale_diff + 7*octave_diff
        
    def _quality(self):
        """Calculate the quality of the interval."""
        pass
        
    def invert(self, direction='up'):
        """Invert the interval."""
        raise NotImplemented

        
def interval(note1, note2):
    """Calculate the interval between two notes."""
    octave_diff = note1.octave - note2.octave
    scale_diff = ord(note1.name) - ord(note2.name) + 1
    note_diff = scale_diff + 7*octave_diff
    return scale_diff, octave_diff, note_diff

def main():
    n1 = Note('F', 5)
    n2 = Note('C')
    print interval(n1, n2)
    
if __name__ == '__main__':
    main()