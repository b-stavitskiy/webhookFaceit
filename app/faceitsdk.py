import requests, flask
import config.settings

class FaceitSDK:
    def __init__(self) -> None:
        self.api_key        = config.settings.FACEIT_API_KEY
        self.owner_key      = config.settings.FACEIT_OWNER_KEY
        self.endpoint_url   = config.settings.FACEIT_ENDPOINT_URL
        self.app_id         = config.settings.FACEIT_APP_ID
        self.webhook_id     = config.settings.FACEIT_WEBHOOK_ID
        self.webhook_name   = config.settings.FACEIT_WEBHOOK_NAME
        self.webhook_url    = config.settings.FACEIT_WEBHOOK_URL

        self.headers = {
            'Authorization': 'Bearer {}' . format(self.api_key),
            'Accept': 'application/json',
        }

        self.ownerHeaders = {
            'Authorization': 'Bearer {}' . format(self.owner_key),
            'Accept': 'application/json',
        }

    def getPlayer(self, name: str) -> dict:
        params = {
            'nickname': name
        }
        url = '{}/players' . format(self.endpoint_url)

        response = requests.get(
            url,
            params=params,
            headers=self.headers
        )

        if (response.status_code != 200):
            flask.abort(404)

        return response.json()

    def appendWebhook(self, playerId: str) -> dict:
        url = 'https://api.faceit.com/webhooks/v1/subscriptions/{}' . format(self.webhook_id)

        response = requests.put(
            url,
            json=self.__getAppendWebhookJson(playerId),
            headers=self.ownerHeaders
        )

        if (response.status_code != 200):
            flask.abort(404)

        return response.json()

    def getRestrictions(self) -> list:
        params = {
            'app_id': self.app_id,
            'limit': 1000,
        }
        url = 'https://api.faceit.com/webhooks/v1/subscriptions'

        response = requests.get(
            url,
            params=params,
            headers=self.ownerHeaders
        )

        if (response.status_code != 200):
            flask.abort(404)

        for dict in response.json()['payload']:
            if (dict['id'] == self.webhook_id):
                return dict['restrictions']

        flask.abort(404)

    def __getAppendWebhookJson(self, playerId: str) -> dict:
        return {
            'active': bool(1),
            'app_id': self.app_id,
            'events': ['match_status_finished'],
            'name': self.webhook_name,
            'public': bool(1),
            'restrictions': self.getRestrictions() + [{
                'type': 'user',
                'value': playerId
            }],
            'tokens': {
                'header_name': '',
                'header_value': '',
                'query_name': '',
                'query_value': '',
            },
            'type': 'user',
            'url': self.webhook_url,
        }

