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

bp = Blueprint('metadata', __name__)


@bp.route('table/<tid>', methods=['GET'])
def get_table(tid: int):
    print(tid)
    # todo 获取表信息
    return ""


@bp.route('table', methods=['POST'])
def create_table():
    # todo 建表
    pass
    return ""


@bp.route('table', methods=['PUT'])
def update_table():
    # todo 修改表
    pass
    return ""


@bp.route('table', methods=['DELETE'])
def delete_table():
    # todo 删除表
    pass
    return ""


@bp.route('column', methods=['POST'])
def table_column_add():
    # todo 新增字段
    return ""


@bp.route('column', methods=['PUT'])
def table_column_update():
    # todo 修改字段
    return ""


@bp.route('column', methods=['DELETE'])
def table_column_delete():
    # todo 删除字段
    return ""
