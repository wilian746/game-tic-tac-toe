from marshmallow import Schema, fields


class PositionSchema(Schema):
    x = fields.Integer(required=True)
    y = fields.Integer(required=True)


class MakeMoveSchema(Schema):
    id = fields.String(required=True)
    player = fields.String(required=True)
    position = fields.Nested(PositionSchema, required=True)
