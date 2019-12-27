from sqlalchemy import Column, String, Date, Integer, Numeric
from app.services.sqlalchemy.sqlalchemy import Base


class MatchModel(Base):
    __tablename__ = 'match'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)
    height = Column(Integer)
    weight = Column(Numeric)

    def __init__(self, name, date_of_birth, height, weight):
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight
