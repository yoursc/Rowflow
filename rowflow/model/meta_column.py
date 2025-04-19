#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
"""
from ExtendRegister.database_register import db


class MetaColumn(db.Model):
    __tablename__ = 'meta_column'
    c_uuid = db.Column(db.String(32), primary_key=True)
    c_name = db.Column(db.String(100), nullable=False)
    c_type = db.Column(db.String(100))
    c_note = db.Column(db.String(100))

    def __init__(self, i_uuid, i_name, i_type, i_note):
        self.c_uuid = i_uuid
        self.c_name = i_name
        self.c_type = i_type
        self.c_note = i_note

    def __repr__(self):
        return f"Column uuid={self.c_uuid}, name={self.c_name}, type={self.c_type}, note={self.c_note}"
