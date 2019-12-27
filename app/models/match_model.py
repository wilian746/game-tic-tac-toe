from sqlalchemy import Column, String
from app.services.sqlalchemy.sqlalchemy import Base


class MatchModel(Base):
    __tablename__ = 'match'
    __table_args__ = {"extend_existing": True}

    id = Column(String, primary_key=True)
    next_player = Column(String)
    winner = Column(String)

    # Lets us print (out a user object conveniently.)
    def __repr__(self):
       return "<Match(id='%s', next_player='%s', winner='%s')>" % (
           self.id, self.next_player, self.winner
       )
