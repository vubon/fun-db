import os
import json


class FunDB(object):

    # def __init__(self, location):
    #     self.location = os.path.expanduser(location)
    #     self.load = self.location

    def set(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        if isinstance(kwargs, dict):
            pass
        else:
            raise ValueError(f"Set value should dictionary{self}")


