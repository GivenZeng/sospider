#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from pony.orm import *
from models import db, Author, Paper, Domain, Publisher


class TestModel(unittest.TestCase):
    def test_author(self):
        with db_session:
            a = Author(author_id='3333')
            a.name = 'given'
            p = Paper(paper_id='qqqq')
            p.title = 'titttttttle'
            a.papers.add(p)

    def test_paper(self):
        with db_session:
            p = Paper(paper_id='666aaaaa66')
            p.title = 'hehehehhehe'


if __name__ == '__main__':
    unittest.main()
