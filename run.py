#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Yoursc
@Date   : 2023-12-25
程序启动入口
"""
import os
import datetime
import platform
import threading
from rowflow import create_app

app = create_app()


def show():
    flask_env = os.environ.get('FLASK_ENV')
    print('<', '-' * 66, '>')
    print('时间:{}'.format(datetime.datetime.now()))
    print('操作系统:{}'.format(platform.system()))
    print('项目路径:{}'.format(os.getcwd()))
    print('当前环境:{}'.format(flask_env))
    print('父进程id:{}'.format(os.getppid()))
    print('子进程id:{}'.format(os.getpid()))
    print('线程id:{}'.format(threading.get_ident()))
    # print(app.url_map)
    print('<', '-' * 66, '>')


def main():
    # Linux服务器启动
    if platform.system() == 'Linux':
        app.run()
    else:
        app.run(debug=True)


if __name__ == '__main__':
    show()
    main()
