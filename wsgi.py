from flask import Flask, jsonify, request

from app.faceitsdk import FaceitSDK

app = Flask(__name__)
sdk = FaceitSDK()

@app.route('/')
def start():
    return 'Hello, World!'

@app.route('/oauthCallback')
def start():
    return jsonify(request.get_json)
