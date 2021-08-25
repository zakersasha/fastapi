from fastapi import FastAPI

from db import metadata, engine, database
from crud.api import producer_router, product_router

app = FastAPI()

metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.disconnect()


app.include_router(product_router)
app.include_router(producer_router)
