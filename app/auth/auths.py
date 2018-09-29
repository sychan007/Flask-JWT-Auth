#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     auths
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'
import  time
from app.users.model import Users

class Auth():

    def error_handler(self, e):
        print(e)
        return "app.auths.Auth.error_handler",400


    def authenticate(self, username, password):
        userInfo = Users.query.filter_by(username=username).first()
        if userInfo is None:
            self.error_handler('找不到用户')
        else:
            if (Users.check_password(Users, userInfo.password, password)):
                login_time = int(time.time())
                userInfo.login_time = login_time
                Users.update(Users)
                return userInfo
            else:
                self.error_handler('密码不正确')


    def identity(self, payload):
        id = payload['identity']
        return Users.get(Users, id)

