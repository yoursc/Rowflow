#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/23
"""
import uuid
from ExtendRegister.database_register import db
from rowflow.model.meta_column import MetaColumn
from rowflow.model.meta_table import MetaTable


def column_get_by_uuid(c_uuid: str) -> MetaColumn:
    r = MetaColumn.query.get(c_uuid)
    return r


def column_get_list_by_table(t_uuid: str) -> list[MetaColumn]:
    cs = MetaColumn.query.filter(MetaColumn.t_uuid == t_uuid).all()
    return cs


def column_create(c_name: str, t_uuid: str, c_type: str = None, c_note: str = None):
    c = MetaColumn()
    c.c_uuid = str(uuid.uuid4())
    c.c_name = c_name
    c.c_type = c_type
    c.c_note = c_note
    c.t_uuid = t_uuid
    msg = None
    try:
        db.session.begin_nested()
        if MetaTable.query.get(c.t_uuid) is None:
            msg = '未找到指定表的t_uuid'
            raise Exception
        if MetaColumn.query.get(c.c_uuid) is not None:
            msg = 'UUID 重复，请重新提交'
            raise Exception
        if MetaColumn.query.filter(MetaColumn.t_uuid == c.t_uuid, MetaColumn.c_name == c.c_name).first() is not None:
            msg = 'c_name 重复'
            raise Exception
        db.session.add(c)
        db.session.commit()
        msg = "success"
    except Exception as e:
        print(e)
        db.session.rollback()
        if msg is None:
            msg = "error"
    return msg


def column_update(c_uuid: str, c_name: str = None, c_type: str = None, c_note: str = None):
    msg = None
    try:
        db.session.begin_nested()
        c = MetaColumn.query.get(c_uuid)
        if c is None:
            msg = 'c_uuid not found'
            raise Exception
        if c_name is not None:
            c.c_name = c_name
        if c_type is not None:
            c.c_type = c_type
        if c_note is not None:
            c.c_note = c_note
        db.session.commit()
        msg = "success"
    except Exception as e:
        print(e)
        db.session.rollback()
        if msg is None:
            msg = "error"
    return msg


def column_delete(c_uuid: str):
    msg = None
    try:
        db.session.begin_nested()
        c = MetaColumn.query.get(c_uuid)
        if c is None:
            msg = f"Column not found"
            raise Exception
        db.session.delete(c)
        db.session.commit()
        msg = "success"
    except Exception as e:
        print(e)
        if msg is None:
            msg = "error"
        db.session.rollback()
    return msg
