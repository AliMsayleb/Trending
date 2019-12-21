from flask import request


def get_client_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
