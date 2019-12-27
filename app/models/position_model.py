from uuid import uuid4
from sqlalchemy.dialects.sqlite import TEXT

from app import app

table_name = "position"


class PositionsModel:
    __tablename__ = table_name
    __table_args__ = (
        app.sqlAlchemy.UniqueConstraint("match_id", "owner", "x", "y"),
    )

    id = app.sqlAlchemy.Column(TEXT, primary_key=True, default=uuid4)
    match_id = app.sqlAlchemy.Column(TEXT, app.sqlAlchemy.ForeignKey("match.id"), nullable=False)
    owner = app.sqlAlchemy.Column(app.sqlAlchemy.String(1), nullable=True)
    x = app.sqlAlchemy.Column(app.sqlAlchemy.Integer, nullable=False)
    y = app.sqlAlchemy.Column(app.sqlAlchemy.Integer, nullable=False)

    def __repr__(self):
        return "<PositionModel('%s')>" % (self.id,)


class PositionExtendModel:
    __tablename__ = table_name
    __table_args__ = {"extend_existing": True}

    class Meta:
        model = PositionsModel

    # 1:N
    match = app.sqlAlchemy.relationship(
        "MatchExtendModel",
        back_populates="positions",
        lazy="noload",
        viewonly=True,
    )
