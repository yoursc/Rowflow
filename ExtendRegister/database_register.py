#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-29
数据库注册器
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def register_database(app: Flask):
    db.init_app(app)


def sql_batch_runner(sql_batch_str: str):
    for sql in sql_batch_str.replace("\n", " ").split(';'):
        if sql.replace(" ", "") == "":
            break
        print("exe:" + sql)
        db.session.execute(text(sql))
        print("execute success")
    print("sql committed")
    db.session.commit()
    pass
