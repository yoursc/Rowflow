#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/23
字段管理蓝图

新增字段、修改字段、删除字段、获取字段列表
"""

from flask import Blueprint, request, jsonify
import controller.metadata_column as ctrl_meta_col
from rowflow.model.metadata_column import cols2dict

bp = Blueprint('metadata_column', __name__)


@bp.route('get', methods=['GET'])
def column_get():
    # todo 数据校验
    c_uuid = request.args['c_uuid']
    column = ctrl_meta_col.get_col(c_uuid)
    if column is None:
        d, msg = None, "error"
    else:
        d = column.get_dict()
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'MetadataColumn',
        'status': None,
        'message': msg,
    })


@bp.route('get_table', methods=['GET'])
def columns_get():
    # todo 数据校验
    t_uuid = request.args['t_uuid']
    columns = ctrl_meta_col.get_cols(t_uuid)
    if not columns:
        d, msg = None, "error"
    else:
        d = cols2dict(columns)
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'list<MetadataColumn>',
        'status': None,
        'message': msg
    })


@bp.route('create', methods=['POST'])
def column_create():
    # todo 数据校验
    column = ctrl_meta_col.column_create(
        t_uuid=request.args['t_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_note=request.args['c_note'],
    )
    if column is None:
        d, msg = None, "error"
    else:
        d = column.get_dict()
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'MetadataColumn',
        'status': None,
        'message': msg,
    })


@bp.route('update', methods=['PUT'])
def table_column_update():
    # todo 数据校验
    column = ctrl_meta_col.column_update(
        c_uuid=request.args['c_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_note=request.args['c_note'],
    )
    if column is None:
        d, msg = None, "error"
    else:
        d = column.get_dict()
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'MetadataColumn',
        'status': None,
        'message': msg,
    })


@bp.route('delete', methods=['DELETE'])
def table_column_delete():
    c_uuid = request.args['c_uuid']
    # todo 数据校验
    column = ctrl_meta_col.column_delete(c_uuid)
    if column is None:
        d, msg = None, "error"
    else:
        d = column.get_dict()
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'MetadataColumn',
        'status': None,
        'message': msg,
    })
