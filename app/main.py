#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'
from flask import Flask

app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()