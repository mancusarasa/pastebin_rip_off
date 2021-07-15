import requests


class WebServer(object):
    """
    Abstracts the communication with a webserver.
    Exposes methods to obtain exisiting pastes and
    to post new ones.
    """
    def __init__(self, url):
        super(WebServer, self).__init__()
        self.url = url

    def get_paste(self, paste_id):
        full_url = 'http://{}/pastes/{}'.format(self.url, paste_id)
        r = requests.get(full_url)
        return r.json(), r.status_code

    def get_all_pastes(self):
        full_url = 'http://{}/pastes/'.format(self.url)
        r = requests.get(full_url)
        return r.json(), r.status_code

    def create_paste(self, text):
        full_url = 'http://{}/pastes/'.format(self.url)
        r = requests.post(full_url, data={'text': text})
        return r.json(), r.status_code
