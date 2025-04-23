#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
"""
from ExtendRegister.database_register import db


class MetadataTable(db.Model):
    __tablename__ = 'meta_table'
    t_uuid = db.Column(db.String(37), primary_key=True)
    t_name = db.Column(db.String(100), nullable=False)
    t_type = db.Column(db.String(100))
    t_note = db.Column(db.String(100))

    def __repr__(self):
        return f"Table uuid={self.t_uuid}, name={self.t_name}, type={self.t_type}, note={self.t_note}"

    def get_dict(self):
        r = {'t_uuid': self.t_uuid,
             't_name': self.t_name,
             't_type': self.t_type,
             't_note': self.t_note
             }
        return r


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
