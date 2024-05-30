#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-21
元数据管理工具
"""
import database


class Metadata(object):
    def __init__(self):
        self.db = database.get_connection()

    def get_tables(self):
        self.db.execute("tables")
        return ""
