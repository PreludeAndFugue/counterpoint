
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