#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from pony.orm import *
import api
from models import Author, Domain
from log import logger


class TEST_DB(unittest.TestCase):
    def test_get(self):
        with db_session:
            a = Author.get(author_id='ded2d8cd-73c6-41c0-bcf7-db2983805231')
            logger.debug(a.organization)
            self.assertEqual(a.name, 'Abraham Silberschatz')

            d = Domain.get(domain_id='1.1')
            logger.debug(d.name)
            self.assertEqual(d.name, '算法与理论')


if __name__ == '__main__':
    unittest.main()
