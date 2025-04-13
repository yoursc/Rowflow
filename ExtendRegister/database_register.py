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


class Sys_Config(db.Model):
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


class Meta_Table(db.Model):
    __tablename__ = 'meta_table'
    t_uuid = db.Column(db.String(32), primary_key=True)
    t_name = db.Column(db.String(100), nullable=False)
    t_type = db.Column(db.String(100))
    t_note = db.Column(db.String(100))

    def __init__(self, i_uuid, i_name, i_type, i_note):
        self.t_uuid = i_uuid
        self.t_name = i_name
        self.t_type = i_type
        self.t_note = i_note

    def __repr__(self):
        return f"Table uuid={self.t_uuid}, name={self.t_name}, note={self.t_note}"


class Meta_Column(db.Model):
    __tablename__ = 'meta_column'
    c_uuid = db.Column(db.String(32), primary_key=True)
    c_name = db.Column(db.String(100), nullable=False)
    c_type = db.Column(db.String(100))
    c_note = db.Column(db.String(100))

    def __init__(self, i_uuid, i_name, i_type, i_note):
        self.c_uuid = i_uuid
        self.c_name = i_name
        self.c_type = i_type
        self.c_note = i_note

    def __repr__(self):
        return f"Column uuid={self.c_uuid}, name={self.c_name}, type={self.c_type}, note={self.c_note}"


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
