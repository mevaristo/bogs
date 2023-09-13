from bogs.database.engine import database_engine as engine
from sqlalchemy import text
import unittest


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        return

    def test_connection(self):
        test_str = 'connection text'

        with engine.connect() as connection:
            result = connection.execute(text(f"select '{test_str}'"))
            self.assertEqual([(test_str, )], result.all())
