#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-19
【视图管理】蓝图

视图：
创建视图、修改视图类型、重命名视图、删除视图

字段：
过滤：
分组：
排序：
"""
from flask import Blueprint

bp = Blueprint('view', __name__)


@bp.route('/create')
def create_view():
    # todo 创建视图处理
    return ""
