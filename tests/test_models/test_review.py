#!/usr/bin/python3
'''
module containing Review class tests
'''

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
    Test class that tests the Review class
    '''

    def test_instance(self):
        '''
        test instance
        '''
        obj = Review()
        self.assertIsInstance(obj, Review, "")


if __name__ == '__main__':
    unittest.main()
