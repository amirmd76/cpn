# -*- coding: utf-8 -*-

import requests
import json

from . import consts


class Client(object):
    authorized = False
    token = None

    def _get_headers(self):
        if self.token is None:
            raise ValueError("Token should hold a value")
        return {u"authorization": u"Token {}".format(self.token)}

    def _authorize(self):
        res = requests.get(consts.AUTHORIZATION_URL, headers=self._get_headers())
        if res.status_code == 203 or res.status_code == 403:
            self.authorized = False
            raise ValueError("Incorrect CPN token")

        self.authorized = True

    def __init__(self, token):
        self.token = token
        if not self.authorized:
            self._authorize()

    def send_notification(self, device_token, content):
        if not self.authorized:
            self._authorize()
        res = requests.get(consts.SEND_URL, headers=self._get_headers(), json={"token": device_token,
                                                                                        "content": content})

        if res.status_code != 200:
            raise Exception(res.text)

    def send_json_notification(self, device_token, content):
        self.send_notification(device_token, json.dumps(content))

    def obtain_token(self):
        if not self.authorized:
            self._authorize()
        res = requests.get(consts.OBTAIN_URL, headers=self._get_headers())

        if res.status_code != 200:
            raise Exception(res.text)
        result = res.json()
        return result["result"]["token"]
