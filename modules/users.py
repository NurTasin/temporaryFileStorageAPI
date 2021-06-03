from flask import jsonify

def authenticate(api_key):
    authorized={
        "Test":"test",
        "0xfoodbabe":"foodbabe"
    }
    if api_key in authorized.keys():
        return authorized[api_key]
    else:
        return False