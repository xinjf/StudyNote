import requests


class ApiSelectmain(object):
    def api_get_selectmain(self, url, headers):
        return requests.get(url, headers=headers)
