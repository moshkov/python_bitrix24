#!/usr/bin/env python
import unittest

from python_bitrix24 import Bitrix24Connection


class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_method(self):
        self.assertTrue(True)

    def testConnection(self):
        connection = Bitrix24Connection("testLogin", "testPassword", "testMainUserName")

if __name__ == '__main__':
    unittest.main()

