# -*- coding: utf-8 -*-
import unittest
from app.model import Model


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.test = Model()

    def tearDown(self):
        del self.test


    ### UNIT TESTS ###
    def testShouldReturnCorrectNumber(self):
        assert self.test.method() == 123, 'method() not returned correct.'





# Run all tests
if __name__ == '__main__':
    unittest.main()