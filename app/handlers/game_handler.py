from app.controllers.game.match.match_controller import MatchController
from app.utils.http.response.response import Response


class GameHandler:
    def __init__(self):
        self._controller = MatchController()
        self._response = Response()

    def create_match(self):
        try:
            result = self._controller.create_match()
            return self._response.send(
                data=result,
                message="All right with the service",
                code="success",
                status=200,
            )
        except Exception as e:
            return self._response.send(
                data=None, message=str(e), code="error", status=500
            )

    def make_move(self, _id: str):
        try:
            result = self._controller.create_match()
            return self._response.send(
                data=result,
                message="All right with the service",
                code="success",
                status=200,
            )
        except Exception as e:
            return self._response.send(
                data=None, message=str(e), code="error", status=500
            )
