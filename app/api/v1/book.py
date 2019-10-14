#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/7 01:49

from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'I am a book of Jasmine'
