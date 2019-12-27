from marshmallow import fields

from app.models.match_model import MatchModel
from app import app


class Fields(app.marshmallow.ModelSchema):
    id = fields.UUID(dump_only=True)
    next_player = fields.String(required=True)


class MatchSchema(Fields):
    class Meta:
        model = MatchModel
        ordered = True
        exclude = ("positions",)


class MatchCompleteSchema(Fields):
    class Meta:
        model = MatchModel
        ordered = True

    positions = fields.Nested(
        "PositionSchema", many=True, exclude=("matches",)
    )
