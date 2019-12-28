from marshmallow import fields

from app.models.position_model import PositionModel
from app import app


class PositionSchema(app.marshmallow.ModelSchema):
    class Meta:
        model = PositionModel
        ordered = True
        exclude = ("matches",)

    id = fields.UUID(dump_only=True)
    match_id = fields.UUID(required=True)
    owner = fields.String(required=True, allow_none=False)
    x = fields.Integer(required=True, allow_none=False)
    y = fields.Integer(required=True, allow_none=False)


class PositionCompleteSchema(PositionSchema):
    class Meta:
        model = PositionModel
        ordered = True

    matches = fields.Nested(
        "MatchCompleteSchema", many=False, exclude=("positions",)
    )
