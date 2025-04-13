#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025-01-23
开发者蓝图

开发阶段使用的部分调试接口
"""

from flask import Blueprint, render_template, request
from ExtendRegister.database_register import sql_batch_runner

bp = Blueprint('dev', __name__)


@bp.route('/')
def index():
    return render_template("dev.html")


@bp.route('/info')
def info():
    return render_template("info.html")


@bp.route('/canary')
def canary():
    return 'App is running now. Your method is ' + request.method


@bp.route('/run_init_sql')
def test():
    with open('db/init.sql', 'r') as f:
        sqls = f.read()
    return sql_batch_runner(sqls)

