#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pony.orm import *
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

db = Database()


class Author(db.Entity):
    author_id = PrimaryKey(str, 255)  # 作者ID
    name = Optional(str, 255)  # 姓名
    image_url = Optional(str, 255)  # 头像
    organization = Optional(str, 255)  # 机构、组织
    home_page = Optional(str, 255)  # 主页
    paper_count = Optional(int)  # 发布文章数目
    citied_count = Optional(int)  # 被引用数
    g_index = Optional(int)
    h_index = Optional(int)
    domains = Set('Domain')  # 研究领域
    papers = Set('Paper')  # 发表的paper


class Domain(db.Entity):
    domain_id = PrimaryKey(str, 255)
    name = Optional(str)
    authors = Set(Author)


class Paper(db.Entity):
    paper_id = PrimaryKey(str, 255)
    title = Optional(str, 10240)
    abstract = Optional(str, 10240)
    cited_num = Optional(int)
    cite_num = Optional(int)
    url = Optional(str, 255)
    authors = Set(Author)
    publisher = Optional('Publisher')

class Publisher(db.Entity):
    publisher_id = PrimaryKey(str)
    name = Optional(str, 255)
    papers = Set(Paper)


db.bind(provider='mysql', host=DB_HOST, port=DB_PORT,
        user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
db.generate_mapping(create_tables=True)
