from marshmallow import fields
from app.models.match_model import MatchModel
from app import app


class Fields(app.marshmallow.ModelSchema):
    id = fields.UUID(dump_only=True)
    next_player = fields.String(required=True)
    winner = fields.String(required=False)


class MatchSchema(Fields):
    class Meta:
        model = MatchModel
        ordered = True

