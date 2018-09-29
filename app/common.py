#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     common
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'

def trueReturn(data, msg):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }

def falseReturn(data, msg):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }