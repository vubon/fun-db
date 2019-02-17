import os
import uuid
import json


class FunDB(object):

    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}

    def _load(self):
        try:
            self.db = json.load(open(self.location, "r"))
        except Exception as err:
            print("Can't open database {}".format(err))

    def set(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        try:
            # self.db[str(key).lower()] = value
            self.db[str(uuid.uuid4())] = {str(key).lower(): value}
            self.dump_db()
        except Exception as err:
            print(err)

    def dump_db(self):
        try:
            json.dump(self.db, open(self.location, "w+"))

        except Exception as err:
            print("Dump error {}".format(err))

    def get(self, pk):
        """
        :param pk:
        :return:
        """
        try:
            return self.db.get(pk)
        except Exception as err:
            print("Can't find data {}".format(err))

    def reset_db(self):
        self.db = {}
        self.dump_db()
