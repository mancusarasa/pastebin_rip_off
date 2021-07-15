import requests

from config import Config


class WriteAPI(object):
    '''
    Abstracts the logic to obtain an existing
    '''
    def __init__(self):
        super(WriteAPI, self).__init__()
        config = Config()
        self.__sql_host = config.get_sql_host()
        self.__sql_port = config.get_sql_port()
        self.__nosql_host = config.get_nosql_host()
        self.__nosql_port = config.get_nosql_port()


    def create_paste(self, text):
        '''
        Creates a paste. First it creates it in the
        NoSQL store, then in the SQL store pointing
        to the entry in the NoSQL store.
        '''
        nosql_url = 'http://{}:{}/pastes/'.format(
            self.__nosql_host,
            self.__nosql_port
        )
        r = requests.post(nosql_url, data={'text': text})
        if r.status_code == 200:
            paste_path = r.json()['paste_path']
            sql_url = 'http://{}:{}/pastes/'.format(
                self.__sql_host,
                self.__sql_port
            )
            r = requests.post(sql_url, data={'paste_path': paste_path})
            return r.json(), r.status_code
        else:
            return {'error': 'unknown error'}, 500
