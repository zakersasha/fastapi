from typing import List

from fastapi_crudrouter import OrmarCRUDRouter

from . import models, schemas

product_router = OrmarCRUDRouter(schema=models.Product, create_schema=schemas.ProductBase)
producer_router = OrmarCRUDRouter(schema=models.Producer, create_schema=schemas.ProducerBase)


@producer_router.get('', respone_model=List[schemas.ProducerOut])
async def get_all():
    return await models.Producer.objects.all()
