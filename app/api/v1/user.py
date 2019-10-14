#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/7 01:49
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('create')
def create_user():
    pass


@api.route('/get')
def get_user():
    return 'I am Jasmine'
