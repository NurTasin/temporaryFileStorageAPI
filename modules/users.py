from flask import jsonify

def authenticate(api_key):
    authorized={
        "admin":"password"
    }
    if api_key in authorized.keys():
        return authorized[api_key]
    else:
        return False