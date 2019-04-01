# -*- coding: utf-8 -*-
"""
Created on Mar 14, 2018

@author: guxiwen
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    from views import main as main__blueprint
    app.config['SECRET_KEY'] = 'hehe'
    app.register_blueprint(main__blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="172.20.19.27", debug=True, port=8000)
