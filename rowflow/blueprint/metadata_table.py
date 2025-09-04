#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-18
表管理蓝图

新增表、重命名表、删除表、获取所有表列表
"""
from flask import Blueprint, request
import controller.metadata_table as ctrl_meta_tab

bp = Blueprint('metadata_table', __name__)


# todo 所有请求未做数据校验


@bp.route('get', methods=['GET'])
def table_get():
    t_uuid = request.args['t_uuid']
    rd = ctrl_meta_tab.get_tab(t_uuid)
    return rd.get_jsonify()


@bp.route('get_my_table_list', methods=['GET'])
def get_my_table_list():
    rd = ctrl_meta_tab.table_search()
    return rd.get_jsonify()


@bp.route('search', methods=['GET'])
def tables_search():
    # todo 增加搜索筛选功能
    rd = ctrl_meta_tab.table_search()
    return rd.get_jsonify()


@bp.route('create', methods=['POST'])
def table_create():
    rd = ctrl_meta_tab.table_create(
        t_name=request.args['t_name'],
        t_type=request.args['t_type'],
        t_desc=request.args['t_desc'],
    )
    return rd.get_jsonify()


@bp.route('update', methods=['PUT'])
def table_update():
    rd = ctrl_meta_tab.table_update(
        t_uuid=request.args['t_uuid'],
        t_name=request.args['t_name'],
        t_type=request.args['t_type'],
        t_desc=request.args['t_desc'],
    )
    return rd.get_jsonify()


@bp.route('delete', methods=['DELETE'])
def table_delete():
    t_uuid = request.args['t_uuid']
    rd = ctrl_meta_tab.table_delete(t_uuid)
    return rd.get_jsonify()
