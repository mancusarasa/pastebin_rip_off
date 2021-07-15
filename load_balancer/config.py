from configparser import ConfigParser


class Config(object):
    '''
    Singleton with the config of the load balancer configuration.
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
        return self.__parser.get('load_balancer','host')

    def get_port_number(self):
        return self.__parser.get('load_balancer','port')

    def get_webservers_urls(self):
        return self.__parser.get('webservers', 'hosts').split(',')
