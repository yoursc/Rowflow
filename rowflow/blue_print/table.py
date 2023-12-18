#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-18
表管理蓝图

表功能计划：
表：
新增表、重庆名表、删除表、获取所有表列表

字段：
新增字段、修改字段、删除字段、获取字段列表

"""
from flask import Blueprint

bp = Blueprint('table', __name__, url_prefix='/table')


@bp.route('/getlist')
def get_table_list():
    # todo 获取表列表
    return ""


@bp.route('/create')
def create_table():
    # todo 建表处理
    return ""


@bp.route('/column/add')
def table_column_add():
    # todo 新增字段
    return ""
