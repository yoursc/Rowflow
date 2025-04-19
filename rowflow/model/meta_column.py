#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/19
"""
from ExtendRegister.database_register import db


class MetaColumn(db.Model):
    __tablename__ = 'meta_column'
    c_uuid = db.Column(db.String(37), primary_key=True)
    c_name = db.Column(db.String(100), nullable=False)
    c_type = db.Column(db.String(100))
    c_note = db.Column(db.String(100))
    t_uuid = db.Column(db.String(37), nullable=False)

    def __repr__(self):
        return f"Column uuid={self.c_uuid}, name={self.c_name}, type={self.c_type}, note={self.c_note}, t_uuid={self.t_uuid}"
