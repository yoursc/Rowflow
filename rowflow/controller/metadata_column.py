#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/23
"""
import uuid
from ExtendRegister.database_register import db
from rowflow.model.metadata_column import MetadataColumn
from rowflow.model.metadata_table import MetadataTable


def get_col(c_uuid: str) -> MetadataColumn:
    r = MetadataColumn.query.get(c_uuid)
    return r


def get_cols(t_uuid: str) -> list[MetadataColumn]:
    rs = MetadataColumn.query.filter(MetadataColumn.t_uuid == t_uuid).all()
    return rs


def column_create(c_name: str, t_uuid: str, c_type: str, c_note: str = None):
    column = MetadataColumn()
    column.c_uuid = str(uuid.uuid4())
    column.c_name = c_name
    column.c_type = c_type
    column.c_note = c_note
    column.t_uuid = t_uuid
    try:
        db.session.begin_nested()
        if MetadataTable.query.get(column.t_uuid) is None:
            raise Exception('未找到指定表的t_uuid')
        if MetadataColumn.query.get(column.c_uuid) is not None:
            raise Exception('UUID 重复，请重新提交')
        if MetadataColumn.query.filter(MetadataColumn.t_uuid == column.t_uuid,
                                       MetadataColumn.c_name == column.c_name).first() is not None:
            raise Exception('c_name 重复')
        db.session.add(column)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        column = None
    return column


def column_update(c_uuid: str, c_name: str = None, c_type: str = None, c_note: str = None):
    try:
        db.session.begin_nested()
        column = MetadataColumn.query.get(c_uuid)
        if MetadataColumn.query.get(column.c_uuid) is None:
            raise Exception('c_uuid 不存在')
        if c_name is not None:
            column.c_name = c_name
        if c_type is not None:
            column.c_type = c_type
        if c_note is not None:
            column.c_note = c_note
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        column = None
    return column


def column_delete(c_uuid: str):
    try:
        db.session.begin_nested()
        column = MetadataColumn.query.get(c_uuid)
        if column is None:
            raise Exception("Column not found")
        db.session.delete(column)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
        column = None
    return column
