from unittest import TestCase
from database import Database
from models import Room, Hotel, Booking

from tests.__mocks__ import (
    room_mock_data,
    hotel_mock_data,
    booking_mock_data
)


class TestModels(TestCase):
    def setUp(self):
        self.db = Database()

        self.hotel = self.db.hotels.insert(**hotel_mock_data)
        self.room = self.db.rooms.insert(**room_mock_data, hotel_id = self.hotel['_id'])
        self.booking = self.db.bookings.insert(**booking_mock_data, room_id = self.room['_id'])

        self.booking_model = Booking.create(self.booking)

    def test_create_booking_model(self):
        self.assertIsInstance(self.booking_model, Booking)
        self.assertEqual(self.booking_model.__dict__, self.booking)

    def test_create_room_assoc_with_booking(self):
        room_model = self.booking_model.room(self.db)

        self.assertIsInstance(room_model, Room)
        self.assertEqual(room_model.__dict__, self.room)

    def test_create_hotel_assoc_with_room(self):
        hotel_model = self.booking_model.room(self.db).hotel(self.db)

        self.assertIsInstance(hotel_model, Hotel)
        self.assertEqual(hotel_model.__dict__, self.hotel)
