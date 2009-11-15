from counterpoint.counterpoint import Note, Interval

n1 = Note('E')
n2 = Note('E', 'flat', 5)

print n1.midi_number
print n2.midi_number
print n2.midi_number - n1.midi_number
print (n2.midi_number - n1.midi_number) % 12


i = Interval(n1, n2)

print i
print repr(i)