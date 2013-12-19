# -*- coding: utf-8 -*-
import json
import unittest
from app.quote import Quote


class QuoteTestCase(unittest.TestCase):

    def setUp(self):
        self.test = Quote()

    def tearDown(self):
        del self.test


    ### UNIT TESTS ###
    def testShouldReturnList(self):
        assert type(self.test.get_data()) is list, 'get_data() not returned correct.'

    def testShouldReturnNonEmptyList(self):
        assert len(self.test.get_data()) > 0, 'get_data() is empty.'

    def testShouldReturnShuffledList(self):
        assert self.test.get_data() != self.test.get_shuffle_data(self.test.get_data()), 'shuffle_data() not returned shuffle.'




# Run all tests
if __name__ == '__main__':
    unittest.main()