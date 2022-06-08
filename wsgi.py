from flask import Flask, jsonify

from app.faceitsdk import FaceitSDK

app = Flask(__name__)
sdk = FaceitSDK()

@app.route('/')
def start():
    return jsonify({ 'key': sdk.getApiKey() })
