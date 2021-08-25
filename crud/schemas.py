from pydantic import BaseModel


class ProducerBase(BaseModel):
    name: str


class ProducerOut(ProducerBase):
    id: int


class ProductBase(BaseModel):
    name: str
    price: float
    producer: int = 1


class ProductOut(BaseModel):
    id: int
    producer: ProducerOut
