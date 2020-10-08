from .model import Model
from .hotel import Hotel


class Room(Model):
    _id = None
    hotel_id = None
    price = None
    capacity = None

    @classmethod
    def create(cls, record):
        instance = cls()

        instance._id = record.get('_id')
        instance.hotel_id = record.get('hotel_id')
        instance.price = record.get('price')
        instance.capacity = record.get('capacity')

        return instance

    def hotel(self, db):
        select_hotel = db.hotels.select(_id=self.hotel_id)

        if not select_hotel:
            return None
        else:
            return Hotel.create(select_hotel[0])
