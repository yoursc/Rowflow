#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-18
表管理蓝图

新增表、重命名表、删除表、获取所有表列表
"""
from flask import Blueprint, request, jsonify
import controller.metadata_table as ctrl_meta_tab
from rowflow.model.metadata_table import tabs2dict

bp = Blueprint('metadata_table', __name__)


@bp.route('get', methods=['GET'])
def table_get():
    # todo 数据校验
    t_uuid = request.args['t_uuid']
    table = ctrl_meta_tab.get_tab(t_uuid)
    if table is None:
        d, msg = None, "error"
    else:
        d = table.get_dict()
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'MetadataTable',
        'status': None,
        'message': msg,
    })


@bp.route('search', methods=['GET'])
def tables_search():
    # todo 数据校验
    # todo 增加搜索筛选功能
    tables = ctrl_meta_tab.table_search()
    if tables is None:
        d, msg = None, "error"
    else:
        d = tabs2dict(tables)
        msg = "success"
    return jsonify({
        'data': d,
        'type': 'list<MetadataTable>',
        'status': None,
        'message': msg,
    })


@bp.route('create', methods=['POST'])
def table_create():
    # todo 数据校验
    table = ctrl_meta_tab.table_create(
        t_name=request.args['t_name'],
        t_type=request.args['t_type'],
        t_note=request.args['t_note'],
    )
    if table is None:
        d, msg = None, "error"
    else:
        d, msg = table.get_dict(), "success"
    return jsonify({
        'data': d,
        'type': 'MetadataTable',
        'status': None,
        'message': msg,
    })


@bp.route('update', methods=['PUT'])
def table_update():
    # todo 数据校验
    table = ctrl_meta_tab.table_update(
        t_uuid=request.args['t_uuid'],
        t_name=request.args['t_name'],
        t_type=request.args['t_type'],
        t_note=request.args['t_note'],
    )
    if table is None:
        d, msg = None, "error"
    else:
        d, msg = table.get_dict(), "success"
    return jsonify({
        'data': d,
        'type': 'MetadataTable',
        'status': None,
        'message': msg,
    })


@bp.route('delete', methods=['DELETE'])
def table_delete():
    # todo 数据校验
    t_uuid = request.args['t_uuid']
    table = ctrl_meta_tab.table_delete(t_uuid)
    if table is None:
        d, msg = None, "error"
    else:
        d, msg = table.get_dict(), "success"
    return jsonify({
        'data': d,
        'type': 'MetadataTable',
        'status': None,
        'message': msg,
    })
