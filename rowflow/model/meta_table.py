#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
"""
from ExtendRegister.database_register import db


class MetaTable(db.Model):
    __tablename__ = 'meta_table'
    t_uuid = db.Column(db.String(37), primary_key=True)
    t_name = db.Column(db.String(100), nullable=False)
    t_type = db.Column(db.String(100))
    t_note = db.Column(db.String(100))

    def __repr__(self):
        return f"Table uuid={self.t_uuid}, name={self.t_name}, type={self.t_type}, note={self.t_note}"


def meta_table_2_json(t: MetaTable):
    if t is None:
        return None
    r = {'t_uuid': t.t_uuid,
         't_name': t.t_name,
         't_type': t.t_type,
         't_note': t.t_note
         }
    return r


def meta_table_list_2_json(tables: [MetaTable]):
    if tables is None:
        return None
    rs = []
    for t in tables:
        rs.append(meta_table_2_json(t))
    return rs
