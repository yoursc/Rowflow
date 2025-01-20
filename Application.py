#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-14
应用构建器
"""

from flask import Flask, render_template, request
from ExtendRegister.config_register import register_config
from ExtendRegister.blueprint_register import register_blueprint
from ExtendRegister.database_register import register_database, db, sql_batch_runner


def create_app() -> Flask:
    # 创建实例
    app = Flask("rowflow", template_folder='./templates')
    # 跨域
    # 注册 CLI
    # 注册 配置
    register_config(app)
    # 注册 拦截器
    # 注册 数据库
    register_database(app)
    # 注册 蓝图
    register_blueprint(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/info')
    def info():
        return render_template("info.html")

    @app.route('/canary')
    def canary():
        return 'App is running now. Your method is ' + request.method

    @app.route('/test')
    def test():
        with open('db/init.sql', 'r') as f:
            sqls = f.read()
            sql_batch_runner(sqls)
        return ""

    # todo 增加登录拦截器

    return app
