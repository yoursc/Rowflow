#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
表管理模型层
"""
import uuid
from ExtendRegister.database_register import db


class MetadataTable(db.Model):
    __tablename__ = 'meta_table'
    t_uuid = db.Column(db.String(15), primary_key=True)
    t_name = db.Column(db.String(100), nullable=False)
    t_type = db.Column(db.String(100), nullable=False)
    t_desc = db.Column(db.String(100))

    def __repr__(self):
        return f"Table t_uuid={self.t_uuid}, t_name={self.t_name}, t_type={self.t_type}, t_desc={self.t_desc}"

    def get_dict(self):
        r = {'t_uuid': self.t_uuid,
             't_name': self.t_name,
             't_type': self.t_type,
             't_desc': self.t_desc
             }
        return r


def table_create(t_name: str, t_type: str, t_desc: str = None) -> MetadataTable:
    tab = MetadataTable()
    tab.t_name = t_name
    tab.t_type = t_type
    tab.t_desc = t_desc
    for i in range(10):
        tab.t_uuid = 'tab_' + str(uuid.uuid4()).replace('-', '')[:11]
        if MetadataTable.query.get(tab.t_uuid) is not None:
            if i == 9:
                raise Exception(f'你TM点真背，连续{i + 1}次生成表UUID都重复，请重新提交')
            continue
    if MetadataTable.query.filter(MetadataTable.t_name == tab.t_name).first() is not None:
        raise Exception('t_name 重复:' + tab.t_name)
    db.session.add(tab)
    return tab


def table_update(t_uuid: str, t_name=None, t_type=None, t_desc=None) -> MetadataTable:
    table = MetadataTable.query.get(t_uuid)
    if table is None:
        raise Exception("Table not found")
    if t_name is not None:
        table.t_name = t_name
    if t_type is not None:
        table.t_type = t_type
    if t_desc is not None:
        table.t_desc = t_desc
    return table


def table_delete(t_uuid: str):
    table = MetadataTable.query.get(t_uuid)
    if table is None:
        raise Exception("Table not found")
    else:
        db.session.delete(table)


def tabs2dict(tables: list[MetadataTable]):
    """
    字典列表转换
    """
    if tables is None:
        return None
    rs = []
    for t in tables:
        rs.append(t.get_dict())
    return rs
