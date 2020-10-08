from unittest import TestCase
from database import Database
from hotel_system import HotelSystem

from tests.__mocks__ import (
    room_mock_data,
    hotel_mock_data,
    booking_mock_data
)


class TestHotelSystem(TestCase):
    def setUp(self):
        self.db = Database()
        self.system = HotelSystem(self.db)

        self.empty_the_database()

    def test_register_hotel(self):
        hotel_model = self.system.register_hotel(hotel_mock_data['name'])

        self.assertEqual(hotel_model.name, hotel_mock_data['name'])
        self.assertEqual(self.db.hotels.data[1]['_id'], hotel_model._id)
        self.assertEqual(self.db.hotels.data[1]['name'], hotel_mock_data['name'])

    def test_add_room(self):
        room_model = self.system.add_room(5, **room_mock_data)

        expected_dict = { '_id': 1, 'hotel_id': 5, **room_mock_data }

        self.assertEqual(room_model.__dict__, expected_dict)
        self.assertEqual(self.db.rooms.data[1], expected_dict)

    def test_get_room(self):
        room_model_existing = self.system.add_room(5, **room_mock_data)
        room_model = self.system.get_room(room_model_existing._id)

        self.assertEqual(room_model.__dict__, room_model_existing.__dict__)

    def test_book_room(self):
        booking_model = self.system.book_room(5, **booking_mock_data)

        expected_dict = { '_id': 1, 'room_id': 5, **booking_mock_data }

        self.assertEqual(booking_model.__dict__, expected_dict)

    def empty_the_database(self):
        self.db.rooms.data.clear
        self.db.hotels.data.clear
        self.db.bookings.data.clear

        self.db.rooms.cursor = 0
        self.db.hotels.cursor = 0
        self.db.bookings.cursor = 0
