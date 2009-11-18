from counterpoint.counterpoint import Note, Interval

n1 = Note('C')
n2 = Note('D')

print n1.octave
print n2.octave
print n2.midi_number - n1.midi_number
print (n2.midi_number - n1.midi_number) % 12

i = Interval(n1, n2)

print i
print i.number
print repr(i)