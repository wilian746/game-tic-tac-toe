from flask_restplus import Resource

from app.handlers.health_handler import HealthHandler
from app.schemas.routes.health_schema import HealthSchema
from app.services.restplus import api

ns = api.namespace(path="/health", name="Health", description="Check service status")

schema = HealthSchema()


@ns.route("")
@api.doc(security=None)
@api.response(code=404, description="not_found")
@api.response(code=500, description="internal_error")
class HealthCollection(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = HealthHandler()

    @api.response(code=200, model=schema.response_health, description="success")
    def get(self):
        """
        Returns registered health
        """
        return self.health.get()
