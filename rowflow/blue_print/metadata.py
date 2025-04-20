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
from rowflow.model.meta_column import meta_column_2_json, meta_column_list_2_json

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
    # todo 数据校验
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
    # todo 数据校验
    msg = ctrl_metadata.table_update(
        t_uuid=request.args['t_uuid'],
        t_name=request.args['t_name'],
        t_type=request.args['t_type'],
        t_note=request.args['t_note'],
    )
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('table', methods=['DELETE'])
def table_delete():
    # todo 数据校验
    t_uuid = request.args['t_uuid']
    msg = ctrl_metadata.table_delete(t_uuid)
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('column', methods=['GET'])
def table_column_get():
    c_uuid = request.args['c_uuid']
    # todo 数据校验
    c = ctrl_metadata.column_get_by_uuid(c_uuid)
    return jsonify({
        'data': meta_column_2_json(c),
        'type': 'MetaColumn',
        'status': None,
        'message': None,
    })


@bp.route('columns', methods=['GET'])
def table_column_get_list_by_table():
    # todo 数据校验
    t_uuid = request.args['t_uuid']
    cs = ctrl_metadata.column_get_list_by_table(t_uuid)
    return jsonify({
        'data': meta_column_list_2_json(cs),
        'type': 'MetaColumn',
        'status': None,
        'message': None,
    })


@bp.route('column', methods=['POST'])
def table_column_add():
    # todo 数据校验
    msg = ctrl_metadata.column_create(
        t_uuid=request.args['t_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_note=request.args['c_note'],
    )
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('column', methods=['PUT'])
def table_column_update():
    # todo 数据校验
    msg = ctrl_metadata.column_update(
        c_uuid=request.args['c_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_note=request.args['c_note'],
    )
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('column', methods=['DELETE'])
def table_column_delete():
    c_uuid = request.args['c_uuid']
    # todo 数据校验
    msg = ctrl_metadata.column_delete(c_uuid)
    return jsonify({
        'status': None,
        'message': msg,
    })
