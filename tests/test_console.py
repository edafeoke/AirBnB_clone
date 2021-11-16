#!/usr/bin/python3
'''
console test module
'''

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test console class
    """

    def setUp(self):
        '''
        setup method
        '''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

if __nmae__ == '__main__':
    unittest.main()
