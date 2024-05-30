#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-29
蓝图注册器
"""
from flask import Flask

import blue_print.metadata
import blue_print.view
import blue_print.row


def register_bp(app: Flask):
    app.register_blueprint(blue_print.metadata.bp, url_prefix='/metadata')
    app.register_blueprint(blue_print.view.bp, url_prefix='/view')
    app.register_blueprint(blue_print.row.bp, url_prefix='/row')
