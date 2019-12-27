from sqlalchemy import Column, String, Integer, ForeignKey
from app.services.sqlalchemy.sqlalchemy import Base
from sqlalchemy.orm import relationship, backref
from app.models.match_model import MatchModel

class PositionModel(Base):
    __tablename__ = 'position'
    __table_args__ = {"extend_existing": True}

    id = Column(String, primary_key=True)
    match_id = Column(String, ForeignKey('match.id'))
    x = Column(Integer)
    y = Column(Integer)
    owner = Column(Integer)

    match = relationship("MatchModel", backref=backref('positions'))

    # Lets us print (out a user object conveniently.)
    def __repr__(self):
       return "<Position(id='%s', match_id='%s', x=%i, y=%i, owner='%s')>" % (
           self.id, self.match_id, self.x, self.y, self.owner
       )
