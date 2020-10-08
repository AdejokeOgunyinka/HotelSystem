from .room import Room
from .model import Model


class Booking(Model):
    _id = None
    room_id = None
    name = None
    paid = None

    @classmethod
    def create(cls, record):
        instance = cls()

        instance._id = record.get('_id')
        instance.room_id = record.get('room_id')
        instance.name = record.get('name')
        instance.paid = record.get('paid')
        return instance

    def room(self, db):
        select_room = db.rooms.select(_id=self.room_id)
        if not select_room:
            return None
        else:
            return Room.create(select_room[0])
