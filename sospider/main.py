#!/usr/bin/python
# -*- coding: UTF-8 -*-


import util
import time
from util import get_names
import api
import db
from log import  logger


def main():
    names = get_names()
    # 是否已经查询该author信息和co、paper
    dealt_authors = {}
    dealt_paper = {}
    for name in names:
        authors = api.search_author(name)
        for author in authors:
            # 已经处理过该author
            if author['id'] in dealt_authors:
                continue
            dealt_authors[author['id']] = True
            # 获取用户信息
            info = api.get_author(author['id'])
            db.upsert_author(info)

            # 查询合作者的信息
            for co in info['co-authors']:
                if co['id'] in dealt_authors:
                    continue
                util.start_get_author_thread(co['id'])
            # 查询paper
            for p in info['papers']:
                # 判断该paper是否已经查询
                if p['id'] in dealt_paper:
                    continue
                dealt_paper[p['id']] = True
                util.start_get_paper_thread(p['id'], author['id'])
            # 每个author停止2s
            time.sleep(1)
        # 每个name停止10s
        time.sleep(10)

if __name__ == '__main__':
    main()