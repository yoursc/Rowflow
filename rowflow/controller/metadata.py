#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-21
元数据管理工具
"""
import database
import uuid
from ExtendRegister.database_register import db
from rowflow.model.meta_table import MetaTable


def table_get_by_uuid(t_uuid: str) -> MetaTable:
    r = MetaTable.query.get(t_uuid)
    return r


def table_get_list() -> [MetaTable]:
    r = MetaTable.query.all()
    return r


def table_create(t_name: str, t_type=None, t_note=None):
    e = MetaTable()
    e.t_uuid = str(uuid.uuid4())
    e.t_name = t_name
    e.t_type = t_type
    e.t_note = t_note
    print(e)
    with db.session.begin_nested():
        if table_get_by_uuid(e.t_uuid):
            print('UUID 重复，重新生成')
            raise Exception
    try:
        db.session.add(e)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return "error"
    return "success"


def table_update():
    pass


class Metadata(object):
    def __init__(self):
        self.db = database.get_connection()

    def get_tables(self):
        db = self.db
        self.db.execute("tables")
        return ""
