import sys
import os
sys.path.append(os.path.abspath("../"))

import unittest
import tokenizertest

suite = unittest.TestSuite()
suite.addTest(tokenizertest.TokenizerTest('test_tokenize'))

testRunner = unittest.TextTestRunner()
testRunner.run(suite)