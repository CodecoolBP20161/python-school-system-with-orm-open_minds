from model.model_base import *
from model.model_school import School
from example_data import cities


class City(BaseModel):
    """  City table based on City model. """
    name = CharField()
    nearest_school = ForeignKeyField(School, related_name='nearest_school', null=True)
    # Import form example_data
    cities = cities

    @staticmethod
    def add_cities():
        for city in City.cities:
            City.create(name=city['city'], nearest_school=School.select().where(School.name==city['nearest_school']))
