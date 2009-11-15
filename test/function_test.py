import unittest
from counterpoint.counterpoint import card_to_ord

class TestFunctions(unittest.TestCase):
    def test_card_to_ord(self):
        tests = [(1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'),
                 (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th'),
                 (11, '11th'), (12, '12th'), (13, '13th'), (14, '14th'),
                 (17, '17th'), (21, '21st'), (22, '22nd'), (23, '23rd'),
                 (24, '24th'), (55, '55th'), (79, '79th'), (101, '101st'),
                 (112, '112th'), (1056, '1056th')]
        for input, output in tests:
            self.assertEqual(card_to_ord(input), output)
            
if __name__ == '__main__':
    unittest.main()