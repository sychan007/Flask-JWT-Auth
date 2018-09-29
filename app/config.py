#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'

DB_USER = 'root'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_DB = 'foc_test'

DEBUG = True
PORT = 8787
HOST = '127.0.0.1'
SECRET_KEY = 'my foc'

JWT_AUTH_URL_RULE = '/login'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://'+ DB_USER + ':' +DB_PASSWORD+'@'+DB_HOST+'/'+DB_DB