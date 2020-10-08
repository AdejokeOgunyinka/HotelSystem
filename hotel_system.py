from models import Room, Hotel, Booking


class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        the_hotel = self.db.hotels.insert(name=name)
        return Hotel.create(the_hotel)

    def add_room(self, hotel_id, **params):
        the_room = self.db.rooms.insert(hotel_id=hotel_id, **params)
        return Room.create(the_room)

    def get_room(self, room_id):
        room_getter = self.db.rooms.select(_id=room_id)
        if not room_getter:
            return None
        else:
            return Room.create(room_getter[0])

    def book_room(self, room_id, **params):
        your_room = self.db.bookings.insert(room_id=room_id, **params)
        return Booking.create(your_room)
