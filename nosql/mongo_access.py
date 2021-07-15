from mongoengine import connect
from mongoengine import Document
from mongoengine import StringField

from config import Config


class Paste(Document):
    text = StringField(required=True, max_length=512)


class MongoAccess(object):
    """
    A simple wrapper to abstact the access to the
    underlying MongoDB. Implemented as a Singleton.
    """
    __instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_.__instance, class_):
            class_.__instance = object.__new__(class_, *args, **kwargs)
        return class_.__instance

    def __init__(self):
        super(MongoAccess, self).__init__()
        self.__db = Config().get_db()
        self.__host = Config().get_host()
        self.__port = Config().get_port()
        self.client = connect(
            db=self.__db,
            host=self.__host,
            port=self.__port
        )

    def get_paste(self, paste_path):
        result = Paste.objects(id=paste_path)
        return {
            'text': result[0].text
        }

    def create_paste(self, text):
        '''
        Creates a paste with the given text.
        Returns the id of the created paste.
        '''
        paste = Paste(text=text)
        return str(paste.save().id)
