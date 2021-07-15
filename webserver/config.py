from configparser import ConfigParser


class Config(object):
    '''
    Singleton with the config of the webserver configuration.
    Exposes methods to obtain the values present in 'config.ini'.
    '''
    __instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_.__instance, class_):
            class_.__instance = object.__new__(class_, *args, **kwargs)
        return class_.__instance

    def __init__(self):
        super(Config, self).__init__()
        self.__parser = ConfigParser()
        self.__parser.read('./config.ini')

    def get_host_number(self):
        return self.__parser.get('webserver','host')

    def get_port_number(self):
        return self.__parser.get('webserver','port')

    def get_sql_host(self):
        return self.__parser.get('sql', 'host')

    def get_sql_port(self):
        return self.__parser.get('sql', 'port')

    def get_nosql_host(self):
        return self.__parser.get('nosql', 'host')

    def get_nosql_port(self):
        return self.__parser.get('nosql', 'port')
