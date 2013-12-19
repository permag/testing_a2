# -*- coding: utf-8 -*-
import json
# testing tools
import unittest
from mock import Mock
# classes to test
from app.quote import *
from app.game import *


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

    def testShouldReturnNextQuote(self):
        quote = self.test.get_next()
        assert type(quote['quote']) is str, 'get_next() quote not returned correct.'
        assert type(quote['author']) is str, 'get_next() author not returned correct.'


class GameTestCase(unittest.TestCase):

    def setUp(self):
        # mocking Quote class
        quoteMock = Mock(Quote)
        # setting return value
        quoteMock.get_next.return_value = {'quote': 'This is a test quote.', 'author': 'Me'}
        # mock as dependency injection into Game class constructor
        self.test = Game(quoteMock)

    def tearDown(self):
        del self.test


    ### UNIT TESTS ###
    def testShouldReturnAQuoteObject(self):
        quote = self.test.get_next_quote()
        assert quote['quote'] == 'This is a test quote.', ''
        assert quote['author'] == 'Me', ''



# Run all tests
if __name__ == '__main__':
    unittest.main()