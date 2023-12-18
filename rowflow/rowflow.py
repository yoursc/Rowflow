#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-14
"""

# todo 导入核心模块

from flask import Flask
from markupsafe import escape

import blue_print.table
import blue_print.view
import blue_print.row

app = Flask(__name__)

app.register_blueprint(blue_print.table.bp)
app.register_blueprint(blue_print.view.bp)
app.register_blueprint(blue_print.row.bp)


@app.route('/canary')
def canary():
    return 'App is running now.'


@app.route('/test/<string:name>')
def test(name):
    print(escape(name))
    return ""


# todo 增加登录拦截器

if __name__ == '__main__':
    app.run()
