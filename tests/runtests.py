#!/usr/bin/env python

import os
import sys
import unittest

def main():
    tests_loader = unittest.TestLoader()
    test_suit = tests_loader.discover(os.path.abspath(os.path.dirname(__file__)))
    unittest.TextTestRunner().run(test_suit)

if __name__ == "__main__":
    main()
