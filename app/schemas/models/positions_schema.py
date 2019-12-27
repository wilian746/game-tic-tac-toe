from marshmallow import fields

from app.models.position_model import PositionsModel
from app import app


class PositionSchema(app.marshmallow.ModelSchema):
    class Meta:
        model = PositionsModel
        ordered = True
        exclude = ("matches",)

    id = fields.UUID(dump_only=True)
    match_id = fields.UUID(required=True)
    owner = fields.String(required=True, allow_none=False)
    x = fields.String(required=True, allow_none=False)
    y = fields.String(required=True, allow_none=False)


class PositionCompleteSchema(PositionSchema):
    class Meta:
        model = PositionsModel
        ordered = True

    matches = fields.Nested(
        "MatchCompleteSchema", many=False, exclude=("positions",)
    )
