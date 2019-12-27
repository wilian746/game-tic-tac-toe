from flask_restplus import fields
from app.services.restplus.restplus import api

from app.utils.restplus.restplus import response_serializer


class HealthSchema:
    def __init__(self):
        self._name = "Health"

    @property
    def health(self):
        return api.model(self._name, self._obj_health)

    @property
    def _obj_health(self):
        return {
            "environment": fields.String(readonly=True),
            "datetime_server": fields.String(readonly=True),
        }

    @property
    def response_health(self):
        return response_serializer(data=self.health, name_model=f"{self._name}_Response")
