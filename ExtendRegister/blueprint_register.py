#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-29
蓝图注册器
"""
from flask import Flask

import blueprint.dev as bp_dev
import blueprint.metadata_table as bp_meta_table
import blueprint.metadata_column as bp_meta_column
import blueprint.view as bp_view
import blueprint.row as bp_row


def register_blueprint(app: Flask):
    app.register_blueprint(bp_dev.bp, url_prefix='/dev')
    app.register_blueprint(bp_meta_table.bp, url_prefix='/metadata/table')
    app.register_blueprint(bp_meta_column.bp, url_prefix='/metadata/column')
    app.register_blueprint(bp_view.bp, url_prefix='/view')
    app.register_blueprint(bp_row.bp, url_prefix='/row')
