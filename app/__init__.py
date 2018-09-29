#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

db = SQLAlchemy()

def create_app(config_filename):
    app =Flask(__name__)
    app.config.from_object(config_filename)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Origin','*')
        if request.method == 'OPTIONS':
            request.headers['Access-Control-Allow-Methods'] = 'GET, POST'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    from app.auth.auths import Auth
    auth = Auth()
    jwt = JWT(app, auth.authenticate, auth.identity)

    from app.users.model import db
    db.init_app(app)

    from app.users.api import init_api
    init_api(app)

    return app