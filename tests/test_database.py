from unittest import TestCase
from database import Database
from database.table import Table


class TestDatabase(TestCase):
    def setUp(self):
        self.db = Database()

        self.room_data = {
            'hotel_id': 1,
            'price': 1000,
            'capacity': 5,
        }

    def test_table_insert(self):
        result = self.db.rooms.insert(**self.room_data)

        self.assertEqual(len(self.db.rooms.data), 1)
        self.assertEqual(result, {'_id': 1, **self.room_data})
        self.assertEqual(list(self.db.rooms.data.values())[0], {'_id': 1, **self.room_data})

    def test_table_select(self):
        insert_result = self.db.rooms.insert(**self.room_data)
        results = self.db.rooms.select(_id = insert_result['_id'])

        self.assertNotEqual(results, [])
        self.assertEqual(results, [insert_result])

    def skip_test_table_fields_validation(self):
        pass
