#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/23
元数据字段控制层
"""
from model.system import db_session_begin_nested, db_session_rollback, db_session_commit
from rowflow.dao.ResponseData import ResponseData
from rowflow.model.metadata_column import MetadataColumn
from rowflow.model.metadata_table import MetadataTable
import rowflow.model.metadata_column as model_metacol


def get_col(c_uuid: str) -> ResponseData:
    rd = ResponseData("search col success", datatype="MetadataColumn")
    try:
        col = MetadataColumn.query.get(c_uuid)
        if col is None:
            rd.status_code, rd.message = 400, "uuid not found"
        else:
            rd.data = col.get_dict()
    except Exception as e:
        rd.status_code, rd.message = 400, "Unknown error.\n" + str(e)
    return rd


def get_cols(t_uuid: str) -> ResponseData:
    rd = ResponseData("search cols success", datatype="list<MetadataColumn>")
    try:
        cols = MetadataColumn.query.filter(MetadataColumn.t_uuid == t_uuid).all()
        if cols is None:
            rd.status_code, rd.message = 400, "uuid not found"
        else:
            rd.data = model_metacol.cols2dict(cols)
    except Exception as e:
        rd.status_code, rd.message = 400, "Unknown error.\n" + str(e)
    return rd


def column_create(t_uuid: str, c_name: str, c_type: str, c_desc: str = None):
    rd = ResponseData("create col success", datatype="MetadataColumn")
    try:
        if MetadataTable.query.get(t_uuid) is None:
            raise Exception('未找到指定表的t_uuid')
        db_session_begin_nested()
        col = model_metacol.column_create(t_uuid, c_name, c_type, c_desc)
        # todo 创建数据列
        db_session_commit()
        rd.data = col.get_dict()
    except Exception as e:
        db_session_rollback()
        rd.status_code, rd.message = 400, "Unknown error.\n" + str(e)
    return rd


def column_update(c_uuid: str, c_name: str = None, c_type: str = None, c_desc: str = None):
    rd = ResponseData("update col success", datatype="MetadataColumn")
    try:
        db_session_begin_nested()
        col = model_metacol.column_update(c_uuid, c_name, c_type, c_desc)
        # todo 修改数据列
        rd.data = col.get_dict()
        db_session_commit()
    except Exception as e:
        db_session_rollback()
        rd.status_code, rd.message = 400, "Unknown error.\n" + str(e)
    return rd


def column_delete(c_uuid: str) -> ResponseData:
    rd = ResponseData("delete col success", datatype="MetadataColumn")
    try:
        db_session_begin_nested()
        model_metacol.column_delete(c_uuid)
        # todo 禁止删除最后一个字段，禁止删除主键
        db_session_commit()
    except Exception as e:
        db_session_rollback()
        rd.status_code, rd.message = 400, "Unknown error.\n" + str(e)
    return rd
