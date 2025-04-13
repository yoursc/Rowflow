#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-15
本地数据库工具类
"""
import sqlite3

db_file = "../db/database.db"


def init_db():
    conn = get_connection()
    with open("../db/init.sql") as file:
        sql = file.read()
    for s in sql.split("/n/n"):
        print(s)
        c = conn.cursor()
        c.execute(s)
    conn.commit()
    conn.close()


def check():
    pass


def get_connection():
    conn = sqlite3.connect(db_file)
    return conn
