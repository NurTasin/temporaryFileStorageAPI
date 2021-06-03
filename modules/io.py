from os import path,remove
from flask import jsonify

def write(username,filename,content):
    actualPath=path.join("data",username,filename)
    actualPath=path.abspath(actualPath)
    print("Writing to: ",actualPath)
    if path.exists(actualPath):
        with open(actualPath,'w') as f:
            f.write(content)
        return jsonify({
            "success":True,
            "created":False
        })
    else:
        with open(actualPath,'w+') as f:
            f.write(content)
        return jsonify({
            "success":True,
            "created":True
        })

def append(username,filename,content):
    actualPath=path.join("data",username,filename)
    actualPath=path.abspath(actualPath)
    print("Appending to: ",actualPath)
    if path.exists(actualPath):
        with open(actualPath,'a') as f:
            f.write(content)
        return jsonify({
            "success":True,
            "created":False
        })
    else:
        with open(actualPath,'a+') as f:
            f.write(content)
        return jsonify({
            "success":True,
            "created":True
        })

def read(username,filename):
    actualPath=path.join("data",username,filename)
    actualPath=path.abspath(actualPath)
    print("Reading from: ",actualPath)
    if path.exists(actualPath):
        with open(actualPath,'r') as f:
            data=f.read()
        return jsonify({
            "success":True,
            "data":data
        })
    else:
        return jsonify({
            "success":False,
            "msg":"Requested file doesn't exists."
        })

def delete(username,filename):
    actualPath=path.join("data",username,filename)
    actualPath=path.abspath(actualPath)
    print("Writing to: ",actualPath)
    if path.exists(actualPath):
        os.remove(abspath)
        return jsonify({
            "success":True
        })
    else:
        return jsonify({
            "success":False,
            "msg":"Requested file doesn't exists"
        })