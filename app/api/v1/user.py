#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/7 01:49
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

api = Redprint('user')


@api.route('create')
def create_user():
    pass


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    return 'I am Jasmine'
