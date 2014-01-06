# -*- coding: utf-8 -*-
import sys, json
# testing tools
import unittest
from mock import Mock
# classes to test
from src.quote import *
from src.game import *


class QuoteTestCase(unittest.TestCase):

    def setUp(self):
        self.quote = Quote()


    def tearDown(self):
        del self.quote


    ### UNIT TESTS ###
    def testShouldRaiseExceptionOnInvalidJsonFile(self):
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


    def testShouldRaiseExceptionOnNoneDataArgument(self):
        raised = False
        try:
            self.quote.get_shuffle_data(None)
        except:
            raised = True
        assert raised, 'shuffle_data() Exception not raised.'


    def testShouldReturnNextQuote(self):
        quote = self.quote.get_next()
        assert type(quote['quote']) is str, 'get_next() string quote not returned correct.'
        assert type(quote['author']) is list, 'get_next() list author not returned correct.'
        assert type(quote['author'][0] is str), 'get_next() string author not returned correct.'


class GameTestCase(unittest.TestCase):

    def setUp(self):
        # mocking Quote class
        quoteMock = Mock(Quote)
        # setting return value
        quoteMock.get_next.return_value = {'quote': 'This is a test quote.', 'author': ['Me', 'Jag']}
        quoteMock.quote_count = 1
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
        assert 'Me' in quote['author'], 'get_next_quote() not returned correct'

   
    def testShouldHaveCorrectInstanceVariablesData(self):
        self.game.new_quote_data()
        assert self.game.quote == 'This is a test quote.', 'quote variable not setted correct.'
        assert 'Me' in self.game.author, 'author variable not setted correct.'

   
    def testShouldReturnQuoteString(self):
        assert type(self.game.get_quote_text()) is str, 'get_quote_text() not returned string.'

   
    def testShouldReturnAuthorString(self):
        self.game.correct = True
        assert type(self.game.get_correct_anwer()) is str, 'get_correct_anwer() True, not returned string.'
        self.game.correct = False
        assert type(self.game.get_correct_anwer()) is str, 'get_correct_anwer() False, not returned string.'

   
    def testShouldReturnTrueIfCorrectAnswer(self):
        self.game.new_quote_data()
        assert self.game.do_answer('Me'), 'do_answer() Correct, not returned True'
        assert self.game.do_answer('Invalid') == False, 'do_answer() Wrong, not returned False'

   
    def testShouldIncreaseScoreOnCorrect(self):
        self.game.new_quote_data()
        score_before = self.game.score
        self.game.do_answer('Me')
        score_after = self.game.score
        assert score_after == (score_before + 1), 'Score not increased on correct.'

   
    def testShouldNotChangeScoreOnWrong(self):
        self.game.new_quote_data()
        score_before = self.game.score
        self.game.do_answer('Invalid')
        assert self.game.score == score_before, 'Score changed on wrong.'


    def testShouldReturnFalseOnNoneAnswerArgument(self):
        self.game.new_quote_data()
        assert self.game.do_answer(None) == False, 'do_answer() None, not returned False'



# Run all tests
if __name__ == '__main__':
    unittest.main()
