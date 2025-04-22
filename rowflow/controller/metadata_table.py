#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-21
元数据管理工具
"""
import uuid
from ExtendRegister.database_register import db
from rowflow.model.meta_table import MetaTable


def table_get_by_uuid(t_uuid: str) -> MetaTable:
    r = MetaTable.query.get(t_uuid)
    return r


def table_get_list() -> list[MetaTable]:
    r = MetaTable.query.all()
    return r


def table_create(t_name: str, t_type=None, t_note=None):
    e = MetaTable()
    e.t_uuid = str(uuid.uuid4())
    e.t_name = t_name
    e.t_type = t_type
    e.t_note = t_note
    msg = None
    try:
        db.session.begin_nested()
        if MetaTable.query.get(e.t_uuid) is not None:
            msg = 'UUID 重复，请重新提交'
            raise Exception
        if MetaTable.query.filter(MetaTable.t_name == t_name).first() is not None:
            msg = 't_name 重复'
            raise Exception
        db.session.add(e)
        db.session.commit()
        msg = "success"
    except Exception as e:
        print(e)
        db.session.rollback()
        if msg is None:
            msg = "error"
    return msg


def table_update(t_uuid: str, t_name: str, t_type=None, t_note=None):
    msg = None
    try:
        db.session.begin_nested()
        t = table_get_by_uuid(t_uuid)
        if t is None:
            msg = f"Table not found"
            raise Exception
        if t_name is not None:
            t.t_name = t_name
        if t_type is not None:
            t.t_type = t_type
        if t_note is not None:
            t.t_note = t_note
        db.session.commit()
        msg = "success"
    except Exception as e:
        print(e)
        if msg is None:
            msg = "error"
        db.session.rollback()
    return msg


def table_delete(t_uuid: str):
    msg = None
    try:
        db.session.begin_nested()
        t = table_get_by_uuid(t_uuid)
        if t is None:
            msg = f"Table not found"
            raise Exception
        # todo 字段清空前，禁止删表
        db.session.delete(t)
        db.session.commit()
        msg = "success"
    except Exception as e:
        print(e)
        if msg is None:
            msg = "error"
        db.session.rollback()
    return msg

