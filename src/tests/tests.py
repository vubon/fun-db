import os
import unittest

from src.FunDB import FunDB
from src.validations import is_valid_uuid


class FunDBTest(unittest.TestCase):

    def setUp(self):
        location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db = FunDB(location + "/fun.db")

    def test_a_reset_db(self):
        self.db.reset_db()

    def test_set(self):
        a = self.db.set("hello", "world")
        self.assertTrue(is_valid_uuid(a))

    def test_get(self):
        a = self.db.set("hello", "world")
        result = self.db.get(a)
        self.assertDictEqual({'hello': 'world'}, result)

    def test_all(self):
        self.db.set("hello", "world")
        self.db.set("Test", "world")
        self.assertEqual(2, len(self.db.all()))

    def test_delete(self):
        pk = self.db.set("hello", "world")
        res = self.db.delete(pk)
        self.assertTrue(res)

    def test_update(self):
        pk = self.db.set("hello", "world")
        values = self.db.update(pk, **{"name": "Roy"})
        self.assertDictEqual({"name": "Roy"}, values)

    def tearDown(self):
        self.db.reset_db()


if __name__ == "__main__":
    unittest.main()
