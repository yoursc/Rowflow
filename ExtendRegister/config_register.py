#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-29
配置注册器
"""

from flask import Flask
from configparser import ConfigParser
import os
import shutil

# TODO 可指定配置文件

config = ConfigParser()


def register_config(app: Flask):
    # 优先加载测试配置
    if os.path.exists('conf/dev.ini'):
        config.read('conf/dev.ini')
    # 加载默认配置文件
    elif os.path.exists('conf/setting.ini'):
        config.read('conf/setting.ini')
    # 没有配置文件，复制模版
    else:
        shutil.copyfile('conf/template.ini', 'conf/setting.ini')
        config.read('conf/setting.ini')
    set_app(app)
    set_mysql(app)


def set_app(app: Flask):
    APP_PORT: int = int(config.get('APP', 'PORT'))
    app.config['PORT'] = APP_PORT


def set_mysql(app: Flask):
    # mysql
    MYSQL_USERNAME = config.get('MYSQL', 'USERNAME')
    MYSQL_PASSWORD = config.get('MYSQL', 'PASSWORD')
    MYSQL_HOSTNAME = config.get('MYSQL', 'HOSTNAME')
    MYSQL_PORT = config.getint('MYSQL', 'PORT')
    MYSQL_DATABASE = config.get('MYSQL', 'DATABASE')
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        MYSQL_USERNAME,
        MYSQL_PASSWORD,
        MYSQL_HOSTNAME,
        MYSQL_PORT,
        MYSQL_DATABASE
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 20
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
