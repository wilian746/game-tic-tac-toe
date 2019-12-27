from flask_restplus import Model

from app.services.restplus.restplus import api


def response_serializer(
    data: Model,
    name_model="Response",
) -> Model:
    return api.inherit(name_model, data)
