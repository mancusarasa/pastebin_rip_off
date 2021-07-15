import requests

from config import Config


class ReadAPI(object):
    '''
    Abstracts the logic to obtain an existing
    paste. Communicates with both the SQL and
    NoSQL store.
    '''
    def __init__(self):
        super(ReadAPI, self).__init__()
        config = Config()
        self.__sql_host = config.get_sql_host()
        self.__sql_port = config.get_sql_port()
        self.__nosql_host = config.get_nosql_host()
        self.__nosql_port = config.get_nosql_port()

    def get_paste(self, paste_id):
        '''
        Obtains the paste with the given hash.
        '''
        sql_url = 'http://{}:{}/pastes/{}'.format(
            self.__sql_host,
            self.__sql_port,
            str(paste_id)
        )
        r = requests.get(sql_url)
        sql_response, sql_status_code = r.json(), r.status_code
        if r.status_code == 404:
            return sql_response, sql_status_code
        paste_path = sql_response['paste_path']
        return self.get_paste_from_nosql_store(paste_path)

    def get_all_pastes(self):
        '''
        Obtains all the existing pastes
        '''
        sql_url = 'http://{}:{}/pastes/'.format(
            self.__sql_host,
            self.__sql_port
        )
        r = requests.get(sql_url)
        sql_response, sql_status_code = r.json(), r.status_code
        if sql_status_code == 200:
            result = []
            # this is extremely inefficient, a single
            # request to the NoSQL store should solve this
            for paste in sql_response['pastes']:
                nosql_response, nosql_status_code = self.get_paste_from_nosql_store(
                    paste['paste_path']
                )
                if nosql_status_code == 200:
                    result.append({
                        'paste_id': paste['paste_id'],
                        'paste': nosql_response['text']
                    })
            status_code = 200
        else:
            result = []
            status_code = 404
        return result, status_code

    def get_paste_from_nosql_store(self, paste_path):
        nosql_url = 'http://{}:{}/pastes/{}'.format(
            self.__nosql_host,
            self.__nosql_port,
            str(paste_path)
        )
        r = requests.get(nosql_url)
        return r.json(), r.status_code
