from functools import wraps
from flask import make_response
from flask import jsonify


def check_error_handler(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except Exception as ex:
            response = make_response(jsonify({"Error": str(ex)}), 500)
        return response
    return decorated