#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/7 01:49
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


@api.route('create')
def create_user():
    pass


@api.route('/>', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.get_or_404(uid)
    return jsonify(
        id=user.id,
        email=user.email,
        nickname=user.nickname
    )


@api.route('/<uid>', methods=['DELETE'])
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        user = User.query.get_or_404(uid)
        user.delete()
    return DeleteSuccess()
