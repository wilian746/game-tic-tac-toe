from http import HTTPStatus


from app.controllers.game.match.match_controller import MatchController
from app.utils.http.response.response import Response

class GameHandler:
    def __init__(self):
        self._response = Response()
        self.match = MatchController()

    def create_match(self):
        return self.match.create_match()


    def make_move(self, _id: str):
        return Response().send(
            data=_id,
            status=HTTPStatus.OK,
        )
