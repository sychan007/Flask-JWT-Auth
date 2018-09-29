#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     api
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'
from flask import jsonify, request
from app.users.model import Users
#from app.auth.auths import Auth
from flask_jwt import jwt_required,current_identity
from .. import common

def init_api(app):
    @app.route('/register', methods= ['POST'])
    def register():
        """
        用户注册
        :return: json
        """
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users(email=email,username=username, password=Users.set_password(Users, password))
        result = Users.add(Users, user)
        if user.id:
            ret = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            return jsonify(common.trueReturn(ret,'用户注册成功'))
        else:
            return jsonify(common.falseReturn('','用户注册失败'))

    # 用户登录接口已由flask-jwt默认定义好，默认路由是"/auth"，可以在配置文件中配置:
    # JWT_AUTH_URL_RULE = '/login'
    # 修改登录接口路由为'/login'
    # 需要注意的是，登录接口的传值要使用 application/json 形式
    #current_identity返回当前提供token解析后的payload信息。

    @app.route('/user')
    @jwt_required()
    def get():
        """
        获取用户信息
        :return: json
        """
        user = Users.get(Users, current_identity.id)
        ret = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        result = common.trueReturn(ret, '请求成功')
        return jsonify(result)