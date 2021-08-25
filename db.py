import databases
import ormar
import sqlalchemy

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///test.db")
engine = sqlalchemy.create_engine("sqlite:///test.db")


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
