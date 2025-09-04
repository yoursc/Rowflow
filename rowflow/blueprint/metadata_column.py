#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/4/23
字段管理蓝图

新增字段、修改字段、删除字段、获取字段列表
"""
from flask import Blueprint, request
import controller.metadata_column as ctrl_meta_col

bp = Blueprint('metadata_column', __name__)


# todo 所有请求未做数据校验


@bp.route('get', methods=['GET'])
def column_get():
    c_uuid = request.args['c_uuid']
    rd = ctrl_meta_col.get_col(c_uuid)
    return rd.get_jsonify()


@bp.route('get_table', methods=['GET'])
def columns_get():
    t_uuid = request.args['t_uuid']
    rd = ctrl_meta_col.get_cols(t_uuid)
    return rd.get_jsonify()


@bp.route('create', methods=['POST'])
def column_create():
    rd = ctrl_meta_col.column_create(
        t_uuid=request.args['t_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_desc=request.args['c_desc'],
    )
    return rd.get_jsonify()


@bp.route('update', methods=['PUT'])
def table_column_update():
    rd = ctrl_meta_col.column_update(
        c_uuid=request.args['c_uuid'],
        c_name=request.args['c_name'],
        c_type=request.args['c_type'],
        c_desc=request.args['c_desc'],
    )
    return rd.get_jsonify()


@bp.route('delete', methods=['DELETE'])
def table_column_delete():
    c_uuid = request.args['c_uuid']
    rd = ctrl_meta_col.column_delete(c_uuid)
    return rd.get_jsonify()
