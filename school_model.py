from models import BaseModel


class School(BaseModel):
    """  School table based on School model. """
    name = CharField()