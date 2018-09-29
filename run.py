#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     run
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'
from app import create_app

app = create_app('app.config')
if __name__=='__main__':
    app.run(host= app.config['HOST'],
            port= app.config['PORT'],
            debug= app.config['DEBUG'])
