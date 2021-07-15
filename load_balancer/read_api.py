import requests

from config import Config


class ReadAPI(object):
    '''
    Abstracts the logic to obtain an existing
    '''
    def __init__(self):
        super(ReadAPI, self).__init__()
        self.__host = Config().get_read_api_host()
        self.__port = Config().get_read_api_port()

    def get_paste(self, paste_id):
        '''
        Obtains the paste with the given hash.
        '''
        url = 'http://{}:{}/pastes/{}'.format(
            self.__host,
            self.__port,
            str(paste_id)
        )
        r = requests.get(url)
        return r.json(), r.status_code

    def get_all_pastes(self):
        '''
        Obtains all the existing pastes
        '''
        url = 'http://{}:{}/pastes/'.format(
            self.__host,
            self.__port
        )
        r = requests.get(url)
        return r.json(), r.status_code
