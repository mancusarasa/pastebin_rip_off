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

    def get_service_host(self):
        return self.__parser.get('nosql','host')

    def get_service_port(self):
        return self.__parser.get('nosql','port')

    def get_host(self):
        return self.__parser.get('mongodb','host')

    def get_port(self):
        return int(self.__parser.get('mongodb','port'))

    def get_db(self):
        return self.__parser.get('mongodb','db')
