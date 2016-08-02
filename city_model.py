from models import BaseModel


class City(BaseModel):
    """  City table based on City model. """
    name = CharField()
    nearest_school = ForeignKeyField(School, related_name='schools')

