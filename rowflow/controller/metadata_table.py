#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-21
元数据表控制层
"""
from model.system import db_session_begin_nested, db_session_rollback, db_session_commit
from rowflow.dao.ResponseData import ResponseData
from rowflow.model.metadata_table import MetadataTable, tabs2dict
import rowflow.model.metadata_table as model_metatab


def get_tab(t_uuid: str) -> ResponseData:
    rd = ResponseData("search table success", datatype="MetadataTable")
    try:
        tab = MetadataTable.query.get(t_uuid)
        if tab is None:
            rd.status_code, rd.message = 400, "uuid not found"
        else:
            rd.data = tab.get_dict()
    except Exception:
        rd.status_code, rd.message = 400, "Unknown error"
    return rd


def table_search() -> ResponseData:
    # todo 增加搜索筛选功能
    rd = ResponseData("get table list success", datatype="list<MetadataTable>")
    try:
        tabs = MetadataTable.query.all()
        if tabs is None:
            rd.message = "Your table list is empty"
            rd.status_code = 200
        else:
            rd.data = tabs2dict(tabs)
    except Exception:
        rd.message = "Unknown error"
        rd.status_code = 404
    return rd


def table_create(t_name: str, t_type: str, t_desc=None) -> ResponseData:
    rd = ResponseData(message="create table success", datatype="MetadataTable")
    try:
        db_session_begin_nested()
        tab = model_metatab.table_create(t_name, t_type, t_desc)
        rd.data = tab.get_dict()
        # todo 创建数据表、创建默认字段
        db_session_commit()
    except Exception as e:
        db_session_rollback()
        print(e)
        rd.status_code, rd.message = 400, "Unknown error"
    return rd


def table_update(t_uuid: str, t_name=None, t_type=None, t_desc=None) -> ResponseData:
    rd = ResponseData(message="update table success", datatype="MetadataTable")
    try:
        db_session_begin_nested()
        table = model_metatab.table_update(t_uuid, t_name, t_type, t_desc)
        rd.data = table.get_dict()
    except Exception as e:
        db_session_rollback()
        print(e)
        rd.status_code, rd.message = 400, "Unknown error"
    return rd


def table_delete(t_uuid: str) -> ResponseData:
    rd = ResponseData(message="Delete table success")
    try:
        db_session_begin_nested()
        model_metatab.table_delete(t_uuid)
        # todo 删去列字段，删除原表
        db_session_commit()
    except Exception as e:
        db_session_rollback()
        rd.status_code, rd.message = 400, "Unknown error.\n" + str(e)
    return rd
