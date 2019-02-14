import os
import json


class FunDB(object):

    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()

    def _load(self):
        self.db = json.loads(open(self.location, "r"))

    def set(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        try:
            self.db[str(key).lower()] = value
            self.dump_db()
        except Exception as err:
            print(err)

    def dump_db(self):
        try:
            json.dump(self.db, open(self.location, "w+"))

        except Exception as err:
            print(f"Dump error {err}")
