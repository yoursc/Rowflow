#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
字段管理模型层
"""
import uuid
from ExtendRegister.database_register import db


class MetadataColumn(db.Model):
    __tablename__ = 'meta_column'
    c_uuid = db.Column(db.String(37), primary_key=True)
    c_name = db.Column(db.String(100), nullable=False)
    c_type = db.Column(db.String(100))
    c_desc = db.Column(db.String(100))
    t_uuid = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"Column c_uuid={self.c_uuid}, c_name={self.c_name}, c_type={self.c_type}, c_desc={self.c_desc}, t_uuid={self.t_uuid}"

    def get_dict(self):
        r = {'c_uuid': self.c_uuid,
             'c_name': self.c_name,
             'c_type': self.c_type,
             'c_desc': self.c_desc,
             't_uuid': self.t_uuid,
             }
        return r


def column_create(t_uuid: str, c_name: str, c_type: str, c_desc: str = None) -> MetadataColumn:
    col = MetadataColumn()
    col.t_uuid = t_uuid
    col.c_name = c_name
    col.c_type = c_type
    col.c_desc = c_desc
    for i in range(10):
        col.c_uuid = 'col_' + str(uuid.uuid4()).replace('-', '')[:11]
        if MetadataColumn.query.get(col.c_uuid) is not None:
            if i == 9:
                raise Exception(f'你TM点真背，连续{i + 1}次生成UUID都重复，请重新提交')
            continue
    if MetadataColumn.query.filter(MetadataColumn.t_uuid == col.t_uuid,
                                   MetadataColumn.c_name == col.c_name).first() is not None:
        raise Exception('c_name 重复:' + col.c_name)
    db.session.add(col)
    return col


def column_update(c_uuid: str, c_name: str = None, c_type: str = None, c_desc: str = None) -> MetadataColumn:
    col = MetadataColumn.query.get(c_uuid)
    if MetadataColumn.query.get(col.c_uuid) is None:
        raise Exception('c_uuid 不存在')
    if c_name is not None:
        col.c_name = c_name
    if c_type is not None:
        col.c_type = c_type
    if c_desc is not None:
        col.c_desc = c_desc
    return col


def column_delete(c_uuid: str):
    column = MetadataColumn.query.get(c_uuid)
    if column is None:
        raise Exception("Column not found")
    db.session.delete(column)


def cols2dict(columns: list[MetadataColumn]):
    """
    字典列表转换
    """
    if columns is None:
        return None
    rs = []
    for c in columns:
        rs.append(c.get_dict())
    return rs
