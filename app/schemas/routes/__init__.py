from flask_restplus import fields
from flask_restplus import Model

from app.services.restplus import api


def pagination_serializer(results: Model, name_model="Pagination") -> Model:
    return api.inherit(
        name_model,
        {
            "results": fields.List(fields.Nested(results)),
            "page": fields.Integer(readonly=True),
            "size": fields.Integer(readonly=True),
            "total_items": fields.Integer(readonly=True),
            "total_pages": fields.Integer(readonly=True),
        },
    )


def response_serializer(
    data: Model,
    name_model="Response",
    name_model_pagination="Pagination",
    pagination=False,
    multiple=False,
) -> Model:
    if pagination:
        data = pagination_serializer(data, name_model_pagination)

    _obj = {
        "status": fields.String(readonly=True),
        "message": fields.String(readonly=True),
        "code": fields.String(readonly=True),
    }

    if multiple:
        _obj["data"] = fields.List(fields.Nested(data))
    else:
        _obj["data"] = fields.Nested(data)

    return api.inherit(name_model, _obj)
