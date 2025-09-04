#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author :   Owen
@Date   :   2025/9/4
响应封装体
"""
from flask import jsonify


class ResponseData(object):
    def __init__(self, message: str = "", status_code: int = 200, datatype: "str" = "", data=None):
        self.message = message
        self.status_code = status_code
        self.data_type = datatype
        self.data = data

    def get_jsonify(self):
        return jsonify({
            'message': self.message,
            'status_code': self.status_code,
            'data_type': self.data_type,
            'data': self.data,
        })
