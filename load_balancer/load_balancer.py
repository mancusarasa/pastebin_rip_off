from config import Config


class LoadBalancer(object):
    """
    Singleton in charge of deciding which webserver
    has to handle the next request. Provides a single
    method that returns the host:port combination of
    the next webhandler, using Round Robin to pick.
    """
    def __init__(self, webhandlers):
        super(LoadBalancer, self).__init__()
        self.__webhandlers = webhandlers
        self.__current_handler = 0

    def get_next_webserver(self):
        result = self.__webhandlers[self.__current_handler]
        N = len(self.__webhandlers)
        self.__current_handler = (self.__current_handler + 1) % N
        return result


balancer = LoadBalancer(Config().get_webservers_urls())
