#!/usr/bin/python
# -*- coding: UTF-8 -*-


import db
import threading
from config import NAMES_PATH
import api
from log import logger
from models import Author,Paper
from pony.orm import *
from concurrent.futures import ThreadPoolExecutor

author_cnt = 0
paper_cnt = 0
executor = ThreadPoolExecutor(100)


def get_names():
    with open(NAMES_PATH, 'r') as f:
        names = []
        for line in f.readlines():
            names.append(line.strip())
    return names


def get_author(id):
    try:
        info = api.get_author(id)
        # logger.debug('author info=%s', info)
        try:
            db.upsert_author(info)
            global author_cnt
            author_cnt = author_cnt + 1
        except:
            logger.debug('error in upsert author')
    except:
        logger.debug('error in get author info')

# 开启一个线程，获取author存到数据库
def start_get_author_thread(id):
    with db_session:
        a = Author.get(author_id=id)
        if a:
            logger.debug('author has existed, author_id=%s', id)
            return
    executor.submit(get_author,id)


def get_paper(id, author_id):
    try:
        info = api.get_paper(id)
        # logger.debug('paper info=%s', info)
        try:
            db.upsert_paper(info, author_id)
            global paper_cnt
            paper_cnt = paper_cnt + 1
        except Exception as e:
            logger.debug(e)
    except:
        logger.debug('error in get paper info')

# 开启一个线程，获取paper，并存储到数据库
def start_get_paper_thread(id, author_id):
    with db_session:
        p = Paper.get(paper_id=id)
        if p:
            logger.debug('paper has existed, paper_id=%s', id)
            return
    executor.submit(get_paper,id,author_id)

def has_get(author_id):
    with db_session:
        a= Author.get(author_id=author_id)
        if a:
            return True
        return False
