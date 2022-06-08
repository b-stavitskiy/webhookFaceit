import os, json, requests, urllib.parse

import config.settings

class FaceitSDK:

    def __init__(self) -> None:
        self.api_key = config.settings.FACEIT_API_KEY

    def getApiKey(self) -> str:
        return self.api_key
