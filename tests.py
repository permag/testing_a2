# -*- coding: utf-8 -*-
import sys, json
# testing tools
import unittest
from mock import Mock
# classes to test
from app.quote import *
from app.game import *


class QuoteTestCase(unittest.TestCase):

    def setUp(self):
        self.quote = Quote()

    def tearDown(self):
        del self.quote


    ### UNIT TESTS ###
    def testShouldThrowException(self):
        raised = False
        try:
            self.quote.get_data('invalid.json')  # invalid input raises exception
        except:
            raised = True
        assert raised, 'get_data() Exception NOT raised.'


    def testShouldReturnList(self):
        assert type(self.quote.get_data()) is list, 'get_data() not returned correct.'

    def testShouldReturnNonEmptyList(self):
        assert len(self.quote.get_data()) > 0, 'get_data() is empty.'

    def testShouldReturnShuffledList(self):
        assert self.quote.get_data() != self.quote.get_shuffle_data(self.quote.get_data()), 'shuffle_data() not returned shuffle.'

    def testShouldReturnNextQuote(self):
        quote = self.quote.get_next()
        assert type(quote['quote']) is str, 'get_next() quote not returned correct.'
        assert type(quote['author']) is str, 'get_next() author not returned correct.'


class GameTestCase(unittest.TestCase):

    def setUp(self):
        # mocking Quote class
        quoteMock = Mock(Quote)
        # setting return value
        quoteMock.get_next.return_value = {'quote': 'This is a test quote.', 'author': 'Me'}
        # mock as dependency injection into Game class constructor
        self.game = Game(quoteMock)

    def tearDown(self):
        del self.game


    ### UNIT TESTS ###
    def testShouldReturnACorrectQuoteObject(self):
        quote = self.game.get_next_quote()
        assert type(quote) is dict, 'get_next_quote() not returned correct type'
        assert len(quote) is 2, 'get_next_quote() not returned correct length'
        assert quote['quote'] == 'This is a test quote.', 'get_next_quote() not returned correct'
        assert quote['author'] == 'Me', 'get_next_quote() not returned correct'

    def testShould(self):
        mock = Mock(Quote)
        assert Game(mock), 'FEL'





# Run all tests
if __name__ == '__main__':
    unittest.main()
