#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/10 16:30


class A:

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        print(exc_type)
        print(exc_tb)

    def do(self):
        bar = 1 / 0
        return bar


a = A()
print(a)
print('---')
with A() as a:
    print(a)
    print('with')
