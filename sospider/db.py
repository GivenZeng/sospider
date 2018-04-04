#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pony.orm import *
from models import Author, Domain, Paper, Publisher
from log import logger
import api

# 将author存储到数据库
def upsert_author(info):
    with db_session:
        a = Author.get(author_id=info['author_id'])
        if a:
            logger.debug('author has existed, author_id=%s', info['author_id'])
            return
        # logger.debug(info)
        author = Author(author_id=info['author_id'])
        author.name = info['name'] if info['name'] else ''
        author.image_url = info['image_url'] if info['image_url'] else ''
        author.organization = info['organization'] if info['organization'] else ''
        author.home_page = info['home_page'] if info['home_page'] else ''
        author.paper_count = info['paper_count']
        author.citied_count = info['cited_count']

        for d in info['domains']:
            if d['id'] == '':
                continue
            ds = Domain.get(domain_id=d['id'])
            if ds:
                author.domains.add(ds)
            else:
                domain = Domain(domain_id=d['id'])
                domain.name = d['name']
                author.domains.add(domain)


# 将paper存储到数据库
def upsert_paper(info, author_id):
    try:
        with db_session:
            publisher_id = info['publisher_id']
            if publisher_id:
                publisher = Publisher.get(publisher_id=publisher_id)
                if publisher:
                    pass
                else:
                    publisher = Publisher(publisher_id=publisher_id)
                    publisher.name = info['publishername']
    except:
        pass
    with db_session:
        p = Paper.get(paper_id=info['paper_id'])
        if p:
            logger.debug('paper has existed, paper_id=%s', info['paper_id'])
            return
        paper = Paper(paper_id=info['paper_id'])
        paper.title = info['title']
        paper.abstract = info['abstract']
        paper.cite_num = info['cite_num']
        paper.cited_num = info['cited_num']

        publisher_id = info['publisher_id']
        if publisher_id:
            publisher = Publisher.get(publisher_id=publisher_id)
            if publisher:
                paper.publisher = publisher

        if author_id is None:
            return
        a = Author.get(author_id=author_id)
        if a:
            paper.authors.add(a)
        else:
            a_info = api.get_author(author_id)
            author = Author(author_id=a_info['author_id'])
            author.name = a_info['name']
            author.image_url = a_info['image_url']
            author.organization = a_info['organization']
            author.home_page = a_info['home_page']
            author.paper_count = a_info['paper_count']
            author.citied_count = a_info['cited_count']
            paper.authors.add(author)
