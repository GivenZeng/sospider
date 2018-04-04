#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from util import get_names


class TestUtil(unittest.TestCase):
    def test_get_name(self):
        names = get_names()
        self.assertEqual(len(names),5150)


if __name__ == '__main__':
    unittest.main()
