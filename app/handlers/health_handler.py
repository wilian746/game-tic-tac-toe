from app.controllers.health.health_controller import HealthController
from app.utils.http.response.response import Response


class HealthHandler:
    def __init__(self):
        self._controller = HealthController()
        self._response = Response()

    def get(self):
        try:
            result = self._controller.verify()
            return self._response.send(
                data=result,
                status=200,
            )
        except Exception as e:
            return self._response.send(
                data=str(e),
                status=500
            )
