#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-18
表管理蓝图

表功能计划：
表：
新增表、重命名表、删除表、获取所有表列表

字段：
新增字段、修改字段、删除字段、获取字段列表

"""
from flask import Blueprint, render_template
from ExtendRegister.database_register import Meta_Table



bp = Blueprint('metadata', __name__)


@bp.route('')
def index():
    return render_template("metadata.html")


@bp.route('table/<tid>', methods=['GET'])
def table_info(tid: int):
    print(tid)
    # todo 获取表信息
    return ""


@bp.route('table', methods=['POST'])
def table_create():
    # todo 建表
    pass
    return ""


@bp.route('table', methods=['PUT'])
def table_update():
    # todo 修改表
    pass
    return ""


@bp.route('table', methods=['DELETE'])
def table_delete():
    # todo 删除表
    pass
    return ""

@bp.route('tables', methods=['GET'])
def table_list():
    tables = Meta_Table.query.all()
    s = ""
    for l in tables:
        s += str(l) + "<br>\n"
    return str(tables)

@bp.route('column', methods=['GET'])
def table_column_get():
    # todo 获取字段信息
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
