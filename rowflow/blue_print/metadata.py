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
from flask import Blueprint, render_template, request, jsonify
import controller.metadata as ctrl_metadata
from rowflow.model.meta_table import meta_table_2_json, meta_table_list_2_json

bp = Blueprint('metadata', __name__)


@bp.route('')
def index():
    return render_template("metadata.html")


@bp.route('table', methods=['GET'])
def table_get():
    t_uuid = request.args['t_uuid']
    t = ctrl_metadata.table_get_by_uuid(t_uuid)
    return jsonify({
        'data': meta_table_2_json(t),
        'data_type': 'MetaTable',
        'status': None,
        'message': None,
    })


@bp.route('table/search', methods=['GET'])
def table_list():
    # todo 增加搜索筛选功能
    tables = ctrl_metadata.table_get_list()
    print(tables)
    print(type(tables))
    return jsonify({
        'data': meta_table_list_2_json(tables),
        'data_type': 'list<MetaTable>',
        'status': None,
        'message': None,
    })


@bp.route('table', methods=['POST'])
def table_create():
    msg = ctrl_metadata.table_create(
        t_name=request.args['t_name'],
        t_type=request.args['t_type'],
        t_note=request.args['t_note'],
    )
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('table', methods=['PUT'])
def table_update():
    # todo 修改表
    pass
    return jsonify({
        'status': None,
        'message': None,
    })


@bp.route('table', methods=['DELETE'])
def table_delete():
    # todo 删除表
    pass
    return ""


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
