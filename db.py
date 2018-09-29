#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     db
   Description :
   Author :       Administrator
   date：          2018-09-28
-------------------------------------------------
   Change Activity:
                   2018-09-28:
-------------------------------------------------
"""
__author__ = 'Administrator'

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app
from app import db

app.config.from_object('app.config')

db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__=='__main__':
    manager.run()