import ormar

from db import MainMeta


class Producer(ormar.Model):
    class Meta(MainMeta):
        pass

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=30)


class Product(ormar.Model):
    class Meta(MainMeta):
        pass

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=30)
    producer = ormar.ForeignKey(Producer, related_name='products')
    price = ormar.Float()
