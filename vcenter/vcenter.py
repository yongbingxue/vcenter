import logging

import requests
from requests.auth import HTTPBasicAuth


class VCenter(object):

    def __init__(self, ip, username, password):
        logging.info("init vcenter")
        self._base_url = f"https://{ip}"

        session = requests.Session()
        session.auth = HTTPBasicAuth(username, password)
        session.verify = False
        headers = {
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
        session.headers = headers

        url = f"{self._base_url}/rest/com/vmware/cis/session/"
        response = session.post(url)

        logging.info(response.text.encode('utf8'))

        self._session = session

    def get(self, url, **kwargs):
        url = self.base_url + url
        return self.session.get(url, **kwargs)

    def post(self, url, **kwargs):
        url = self.base_url + url
        return self.session.post(url, **kwargs)

    def put(self, url, **kwargs):
        url = self.base_url + url
        return self.session.put(url, **kwargs)

    def patch(self, url, **kwargs):
        url = self.base_url + url
        return self.session.patch(url, **kwargs)

    def delete(self, url, **kwargs):
        url = self.base_url + url
        return self.session.delete(url, **kwargs)

    @property
    def session(self):
        return self._session

    @property
    def base_url(self):
        return self._base_url
