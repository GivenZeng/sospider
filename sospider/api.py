#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

from config import ACCESS_TOKEN,DEBUG
from log import logger


# get the info of the author
# return info and papers at most 50
# return {author_id,name,image_url,origization,domains,home_page,paper_count,cite_count,
# 			co_authors[{id,name,orig_name}...],papers[{id,title,authorsname,publisher}...]}
def get_author(id):
    url = 'http://m.soscholar.com/authors/detail'
    payload = {'access_token': ACCESS_TOKEN,
               'author_id': id, 'paper_page': 1, 'paper_count': 50}
    r = requests.get(url, params=payload)
    result = r.json()
    return result


# get paper by paper_id
def get_paper(id):
    url = 'http://m.soscholar.com/papers/detail'
    payload = {'access_token': ACCESS_TOKEN, 'paper_id': id}
    r = requests.get(url, params=payload)
    result = r.json()
    return result


# get authors by name search
# return {total,has_next,authors[{id,name,image_url,org_name}...]} 
def search_author(name):
    url = 'http://m.soscholar.com/search/authors'
    payload = {'access_token': ACCESS_TOKEN,
               'keyword': name, 'page': 1, 'count': 100}
    has_next = True
    result = {'total': 0, 'authors': []}
    while has_next:
        r = requests.get(url, params=payload)
        try:
            temp = r.json()
        except:
            logger.debug('get error in json decode,str=%s',r)
            continue
        result['total'] += len(temp['authors'])
        result['authors'].extend(temp['authors'])
        if temp['has_next'] == 'true' or temp['has_next']:
            has_next = True
            payload['page'] = payload['page'] + 1
            # 如果是debug就只请求第一页
            if DEBUG:
                break
        else:
            break
    logger.debug('author search name=%s, result len=%d', name,result['total'])
    return result['authors']
