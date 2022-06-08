import flask

from app.faceitsdk import FaceitSDK

app = flask.Flask(__name__)
sdk = FaceitSDK()

@app.route('/<string:name>')
def getPlayer(name):
    player = sdk.getPlayer(name)
    return sdk.appendWebhook(player['player_id'])
