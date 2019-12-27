from uuid import uuid4
from sqlalchemy.dialects.sqlite import TEXT
from app import app
table_name = "match"


class MatchModel:
    __tablename__ = table_name

    id = app.sqlAlchemy.Column(TEXT, primary_key=True, default=uuid4)
    next_player = app.sqlAlchemy.Column(app.sqlAlchemy.String(1), nullable=False)

    def __repr__(self):
        return "<MatchModel('%s')>" % (self.id,)


class MatchExtendModel:
    __tablename__ = table_name
    __table_args__ = {"extend_existing": True}

    class Meta:
        model = MatchModel

    # N:1
    positions = app.sqlAlchemy.relationship("PositionExtendModel", back_populates="matches", lazy="noload")

    def __repr__(self):
        return "<MatchExtendModel('%d')>" % (self.id,)
