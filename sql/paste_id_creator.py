from os import urandom
from binascii import b2a_hex
from hashlib import md5


class PasteIdCreator(object):
    """
    Abstracts the creation of a paste_id (ie a unique hash
    that identifies it in the object store) for a given
    text.
    """
    def __init__(self):
        super(PasteIdCreator, self).__init__()
        self.__urandom_length = 64
        self.__id_length = 10

    def create_paste_id(self):
        # to create the hash, we'll just
        # read some shit from /dev/urandom
        random_string = b2a_hex(urandom(self.__urandom_length))
        # then we'll calculate the md5_hash over the random
        # string, reverse it, and truncate its length
        md5_hash = md5(random_string).hexdigest()
        reversed_hash = md5_hash[::-1]
        return reversed_hash[:self.__id_length]
