#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-29
配置注册器
"""
import os

from flask import Flask


def conf_register(app: Flask):
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'rowflow.sqlite'),
    )
    # todo 后续独立出配置文件
