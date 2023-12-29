#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-14
应用构建器
"""

from flask import Flask, render_template

from ExtendRegister.bp_register import register_bp
from controller.meta import Meta


def create_app():
    # 创建实例
    app = Flask(__name__, template_folder='./templates')
    # 跨域
    # 注册 CLI
    # 注册 配置
    # 注册 拦截器
    # 注册 数据库
    # 注册 蓝图
    register_bp(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/canary')
    def canary():
        return 'App is running now.'

    @app.route('/test')
    def test():
        m = Meta()
        m.get_tables()
        return ""

    # todo 增加登录拦截器

    return app
