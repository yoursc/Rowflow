#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-21
元数据管理工具
"""
import uuid
from ExtendRegister.database_register import db
from rowflow.model.metadata_table import MetadataTable


def get_tab(t_uuid: str) -> MetadataTable:
    r = MetadataTable.query.get(t_uuid)
    return r


def table_search() -> list[MetadataTable]:
    # todo 增加搜索筛选功能
    r = MetadataTable.query.all()
    return r


def table_create(t_name: str, t_type=None, t_note=None) -> MetadataTable:
    table = MetadataTable()
    table.t_uuid = str(uuid.uuid4())
    table.t_name = t_name
    table.t_type = t_type
    table.t_note = t_note
    try:
        db.session.begin_nested()
        if MetadataTable.query.get(table.t_uuid) is not None:
            raise Exception('UUID 重复，请重新提交')
        if MetadataTable.query.filter(MetadataTable.t_name == t_name).first() is not None:
            raise Exception('t_name 重复:' + t_name)
        db.session.add(table)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        table = None
    # todo 建表后自动创建默认字段
    return table


def table_update(t_uuid: str, t_name: str, t_type=None, t_note=None) -> MetadataTable:
    try:
        db.session.begin_nested()
        table = MetadataTable.query.get(t_uuid)
        if table is None:
            raise Exception("Table not found")
        if t_name is not None:
            table.t_name = t_name
        if t_type is not None:
            table.t_type = t_type
        if t_note is not None:
            table.t_note = t_note
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        table = None
    return table


def table_delete(t_uuid: str):
    try:
        db.session.begin_nested()
        table = MetadataTable.query.get(t_uuid)
        if table is None:
            raise Exception("Table not found")
        db.session.delete(table)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        table = None
    return table
