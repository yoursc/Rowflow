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

import re

db = SQLAlchemy()


class SysConfig(db.Model):
    __tablename__ = 'sys_config'
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.String(100), nullable=False)
    k = db.Column(db.String(100), nullable=False)
    v = db.Column(db.String(100))

    def __init__(self, app, k, v):
        self.app = app
        self.k = k
        self.v = v

    def __repr__(self):
        return f"Sys_Config('{self.app}', '{self.k}', '{self.v}')"


def register_database(app: Flask):
    db.init_app(app)


def sql_batch_runner(sql_batch_str: str):
    out_full = []
    for sql in sql_batch_str.replace("\n", " ").split(';'):
        if sql.replace(" ", "") == "":
            break
        sql = re.sub(r'\s+', ' ', sql).strip()

        a = "exe:[" + sql + "]"
        print(a)
        out_full.append(a)

        db.session.execute(text(sql))

        a = "execute success"
        print(a)
        out_full.append(a)

    a = "sql committed"
    print(a)
    out_full.append(a)

    db.session.commit()
    pp = "<br>\n".join(out_full)
    print(pp)
    return pp
