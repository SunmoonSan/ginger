#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2019/10/7 01:30
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


# @app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e

    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg=msg, code=code, error_code=error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e
        # return ServerError()


if __name__ == '__main__':
    app.run(debug=True)
