#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/23
"""
from flask import Blueprint, request, jsonify
import controller.metadata_column as ctrl_meta_col
from rowflow.model.meta_column import meta_column_2_json, meta_column_list_2_json

bp = Blueprint('metadata_column', __name__)


@bp.route('get', methods=['GET'])
def table_column_get():
    c_uuid = request.args['c_uuid']
    # todo 数据校验
    c = ctrl_meta_col.column_get_by_uuid(c_uuid)
    return jsonify({
        'data': meta_column_2_json(c),
        'type': 'MetaColumn',
        'status': None,
        'message': None,
    })


@bp.route('search', methods=['GET'])
def table_column_get_list_by_table():
    # todo 数据校验
    t_uuid = request.args['t_uuid']
    cs = ctrl_meta_col.column_get_list_by_table(t_uuid)
    return jsonify({
        'data': meta_column_list_2_json(cs),
        'type': 'MetaColumn',
        'status': None,
        'message': None,
    })


@bp.route('create', methods=['POST'])
def table_column_create():
    # todo 数据校验
    msg = ctrl_meta_col.column_create(
        t_uuid=request.args['t_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_note=request.args['c_note'],
    )
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('update', methods=['PUT'])
def table_column_update():
    # todo 数据校验
    msg = ctrl_meta_col.column_update(
        c_uuid=request.args['c_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_note=request.args['c_note'],
    )
    return jsonify({
        'status': None,
        'message': msg,
    })


@bp.route('delete', methods=['DELETE'])
def table_column_delete():
    c_uuid = request.args['c_uuid']
    # todo 数据校验
    msg = ctrl_meta_col.column_delete(c_uuid)
    return jsonify({
        'status': None,
        'message': msg,
    })
