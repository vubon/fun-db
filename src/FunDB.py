import os
import uuid
import json

# Import logger file
from .logger import logger_file
from .validations import is_valid_uuid

# giving logger file name
logger = logger_file.getLogger('general')
access_logger = logger_file.getLogger('access')


class FunDB(object):

    def __init__(self, location):
        self.location = os.path.expanduser(location)
        if os.path.exists(self.location):
            self._load()
        else:
            self.db = {}
            self._dump_db()

    def _load(self):
        """Load the database from the file."""
        try:
            with open(self.location, "r") as reader:
                self.db = json.load(reader)
                access_logger.info(f"Database loaded successfully: {self.db}")
        except FileNotFoundError:
            logger.error(f"Database file not found at {self.location}")
            self.db = {}
        except json.JSONDecodeError:
            logger.error(f"Database file is corrupted at {self.location}")
            self.db = {}
        except Exception as err:
            logger.error(f"Failed to load database: {err}")
            self.db = {}

    def set(self, key, value):
        """
        Set a value in the database.
        :param key: The key under which the value is stored.
        :param value: The value to store.
        :return: The UUID of the stored record.
        """
        try:
            pk = str(uuid.uuid4())
            self.db[pk] = {str(key).lower(): value}
            self._dump_db()  # Persist changes immediately
            access_logger.info(f"Data set successfully: {pk} -> {self.db[pk]}")
            return pk
        except Exception as err:
            logger.error(f"Data set error: {err}")
            return None

    def get(self, pk):
        """
        Get a value from the database by its primary key (UUID).
        :param pk: The UUID key.
        :return: The value associated with the key, or None if not found.
        """
        if not is_valid_uuid(pk):
            logger.error(f"Invalid UUID provided: {pk}")
            return None

        try:
            return self.db[pk]
        except KeyError:
            logger.error(f"Key not found: {pk}")
            return None
        except Exception as err:
            logger.error(f"Error retrieving data: {err}")
            return None

    def all(self):
        """
        Get all records from the database.
        :return: All records in the database.
        """
        try:
            return self.db
        except Exception as err:
            logger.error(f"Can't load data: {err}")
            return {}

    def delete(self, pk) -> bool:
        """
        Delete a record from the database by its primary key.
        :param pk: The UUID key of the record to delete.
        :return: True if the record was deleted, False otherwise.
        """
        if not is_valid_uuid(pk):
            logger.error(f"Invalid UUID provided for deletion: {pk}")
            return False

        try:
            del self.db[pk]
            self._dump_db()  # Persist changes immediately
            access_logger.info(f"Deleted record with key: {pk}")
            return True
        except KeyError:
            logger.error(f"Key not found for deletion: {pk}")
            return False
        except Exception as err:
            logger.error(f"Error deleting data: {err}")
            return False

    def update(self, pk, **kwargs):
        """
        Update an existing record in the database by its primary key.
        :param pk: The UUID key of the record to update.
        :param kwargs: The new data to store.
        :return: The updated data or None if the key does not exist.
        """
        obj = self.get(pk)
        if obj is None:
            logger.error(f"Cannot update non-existing record: {pk}")
            return None

        self.db[pk] = kwargs
        self._dump_db()  # Persist changes immediately
        access_logger.info(f"Updated record with key: {pk}")
        return kwargs

    def reset_db(self):
        """Reset the database by clearing all records."""
        self.db = {}
        self._dump_db()  # Persist changes immediately
        access_logger.info("Database reset")

    def _dump_db(self):
        """Persist the current state of the database to the file."""
        try:
            with open(self.location, "w") as writer:
                json.dump(self.db, writer)
                access_logger.info(f"Database successfully dumped to {self.location}")
        except Exception as err:
            logger.error(f"Error dumping database: {err}")
