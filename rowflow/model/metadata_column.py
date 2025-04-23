#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
"""
from ExtendRegister.database_register import db


class MetadataColumn(db.Model):
    __tablename__ = 'meta_column'
    c_uuid = db.Column(db.String(37), primary_key=True)
    c_name = db.Column(db.String(100), nullable=False)
    c_type = db.Column(db.String(100))
    c_note = db.Column(db.String(100))
    t_uuid = db.Column(db.String(37), nullable=False)

    def __repr__(self):
        return f"Column uuid={self.c_uuid}, name={self.c_name}, type={self.c_type}, note={self.c_note}, t_uuid={self.t_uuid}"

    def get_dict(self):
        r = {'c_uuid': self.c_uuid,
             'c_name': self.c_name,
             'c_type': self.c_type,
             'c_note': self.c_note,
             't_uuid': self.t_uuid,
             }
        return r


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
