from .model import Model


class Hotel(Model):
    _id = None
    name = None

    @classmethod
    def create(cls, record):
        instance = cls()

        instance._id = record.get('_id')
        instance.name = record.get('name')
        return instance
