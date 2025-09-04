#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/9/5
"""
from ExtendRegister.database_register import db
import re
from sqlalchemy import text


def db_session_begin_nested():
    db.session.begin_nested()


def db_session_commit():
    db.session.commit()


def db_session_rollback():
    db.session.rollback()


def sql_batch_runner(sql_batch_str):
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
