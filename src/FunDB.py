import os
import uuid
import json

# Import logger file
from .logger import logger_file

# giving logger file name
logger = logger_file.getLogger('general')
access_logger = logger_file.getLogger('access')


class FunDB(object):

    def __init__(self, location):
        self.location = os.path.expanduser(location)
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}

    def _load(self):
        try:
            self.db = json.load(open(self.location, "r"))
            access_logger.info(f'Reading Database {self.db}')
        except Exception as err:
            logger.error("Can't open database {}".format(err))

    def set(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        try:
            self.db[str(uuid.uuid4())] = {str(key).lower(): value}
            return self.dump_db()
        except Exception as err:
            logger.error("Data set error {}".format(err))

    def dump_db(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
        except Exception as err:
            logger.error("Dump error {}".format(err))

        return list(self.db)[-1]

    def get(self, pk):
        """
        :param pk:
        :return:
        """
        try:
            return self.db[pk]
        except Exception as err:
            logger.error("Can't find data {}".format(err))

    def all(self):
        """
        :return:
        """
        try:
            return self.db
        except Exception as err:
            logger.error("Con't load data {}".format(err))

    def delete(self, pk):
        try:
            del self.db[pk]
            self.dump_db()
            return True
        except Exception as err:
            logger.error("Item can't delete {}".format(err))
            return False

    def reset_db(self):
        self.db = {}
        self.dump_db()
        access_logger.info('Database reset')
