import unittest
from names_all import full_names


class NamesTest(unittest.TestCase):

    def test_all_names(self):
        full_all = full_names('munyange', 'ford')
        self.assertEqual(full_all, 'Munyange Ford')

    # adding a test for the middle name
    def test_middle(self):
        full_all = full_names('clapper', 'wanja', 'abbot')

        self.assertEqual(full_all, 'Clapper Abbot Wanja')


unittest.main()
"""
adding a third positional argument in the full_names() function without updating the test file
return a TypeError of a missing argument. 

Do not change the test file to fix the error - treat this file as the ideal of your program - instead,
fix your program so that it passes the test. 
"""
# Additional Methods
"""
#verify that a value a is equal or not equal to a value b
assertEqual(a, b)
assertNotEqual(a, b)

#verify that a value -x is true or false
assertTrue(x)
assertFalse(x)

#verify that an item is within a list 
assertIn(item, list)
assertIn(item, list)
"""
