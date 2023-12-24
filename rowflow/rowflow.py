#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-14
"""
from flask import Flask, render_template
from controller.meta import Meta

import blue_print.table
import blue_print.view
import blue_print.row


def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.register_blueprint(blue_print.table.bp)
    app.register_blueprint(blue_print.view.bp)
    app.register_blueprint(blue_print.row.bp)

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
