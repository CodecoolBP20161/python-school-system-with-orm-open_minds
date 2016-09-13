from model.model_base import *
from example_data import schools


class School(BaseModel):
    """  School table based on School model. """
    name = CharField()
    # import from example_data
    schools = schools

    @staticmethod
    def add_schools():
        for school in School.schools:
            School.create(name=school['name'])
