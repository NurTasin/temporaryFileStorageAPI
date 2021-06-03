from modules import io
from modules import users

from flask import Flask, jsonify, request

app=Flask(__name__)
@app.route("/api/v1/",methods=["GET"])
def INSTRUCTIONS():
    return jsonify({
        "msg":"Welcome to temp.io API version 1.0.0 . If you are registered then try a POST request with api key in x-api-key feild.",
        "docs":"temp.io/docs/v1/"
    })

@app.route("/api/v1/",methods=["POST"])
def HOME():
    try:
        apiKey=request.json["x-api-key"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not provided."
        })
    
    except TypeError:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not provided."
        })
    if users.authenticate(apiKey)!=False:
        return jsonify({
            "success":True,
            "msg":"Authenticated successfully."
        })
    else:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not matched"
        })


@app.route("/api/v1/read/",methods=["POST"])
def RequestReadFile():
    try:
        apiKey=request.json["x-api-key"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not provided."
        })
    except TypeError:
        return jsonify({
            "success":False,
            "msg":"value for x-api-key field not provided."
        })
    
    try:
        addr=request.json["path"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"value for path field not provided."
        })
    
    if ".." in addr:
        return jsonify({
            "success":False,
            "msg":"for security perposes, we don't allow using '..' path"
        })
    
    if users.authenticate(apiKey)!=False:
        return io.read(users.authenticate(apiKey),addr)
    else:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not matched."
        })

@app.route("/api/v1/write/",methods=["POST"])
def RequestWriteFile():
    try:
        apiKey=request.json["x-api-key"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not provided."
        })
    except TypeError:
        return jsonify({
            "success":False,
            "msg":"value for x-api-key field not provided."
        })
    
    try:
        addr=request.json["path"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"value for path field not provided."
        })
    
    if ".." in addr:
        return jsonify({
            "success":False,
            "msg":"for security perposes, we don't allow using '..' path"
        })
    
    try:
        content=request.json["content"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"value for content field not provided."
        })
    if users.authenticate(apiKey)!=False:
        return io.write(users.authenticate(apiKey),addr,content)
    else:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not matched."
        })

@app.route("/api/v1/append/",methods=["POST"])
def RequestAppendFile():
    try:
        apiKey=request.json["x-api-key"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not provided."
        })
    except TypeError:
        return jsonify({
            "success":False,
            "msg":"value for x-api-key field not provided."
        })
    
    try:
        addr=request.json["path"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"value for path field not provided."
        })
    
    if ".." in addr:
        return jsonify({
            "success":False,
            "msg":"for security perposes, we don't allow using '..' path"
        })
    
    try:
        content=request.json["content"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"value for content field not provided."
        })
    if users.authenticate(apiKey)!=False:
        return io.append(users.authenticate(apiKey),addr,content)
    else:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not matched."
        })

@app.route("/api/v1/remove")
def RequestRemoveFile():
    try:
        apiKey=request.json["x-api-key"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not provided."
        })
    except TypeError:
        return jsonify({
            "success":False,
            "msg":"value for x-api-key field not provided."
        })
    
    try:
        addr=request.json["path"]
    except KeyError:
        return jsonify({
            "success":False,
            "msg":"value for path field not provided."
        })
    
    if ".." in addr:
        return jsonify({
            "success":False,
            "msg":"for security perposes, we don't allow using '..' path"
        })
    
    if users.authenticate(apiKey)!=False:
        return io.delete(users.authenticate(apiKey),addr)
    else:
        return jsonify({
            "success":False,
            "msg":"Authentication Failed. API Key not matched."
        })

if __name__=="__main__":
    app.run(port=8080,debug=True)