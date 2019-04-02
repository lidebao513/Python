#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mar 14, 2018


"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    from views import main as main__blueprint
    app.config['SECRET_KEY'] = 'xiaobao'
    app.register_blueprint(main__blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="10.40.48.241", debug=True, port=8000)
    # app.run(host="192.168.0.103", debug=True, port=8000)
# 在哪台机器上的IP启动端口号
# 写自己的IP地址 setuptools
# 该文件为启动文件 负责启动该服务