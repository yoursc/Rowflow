#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-19
【数据行】蓝图
"""
from flask import Blueprint

bp = Blueprint('row', __name__, url_prefix='row')


@bp.route('/add')
def row_add():
    return ""
