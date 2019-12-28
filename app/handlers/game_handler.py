from http import HTTPStatus
from flask import request

from app.controllers.game.match.match_controller import MatchController
from app.utils.http.response.response import Response
from app.schemas.models.make_move_schema import MakeMoveSchema

class GameHandler:
    def __init__(self):
        self._response = Response()
        self.match = MatchController()

    def create_match(self):
        return self.match.create_match()

    def make_move(self, match_id: str):
        body = request.get_json(silent=True, force=True)
        data, errors = MakeMoveSchema().load(data=body)
        if errors or len(match_id) == 0:
            return self._response.send(
                data={
                    "msg": "Os dados enviados não estão no padrão veja na documentação e tente novamente!",
                    "errors": errors
                },
                status=HTTPStatus.BAD_REQUEST,
            )
        if str.upper(data.get("player")) != "X" and str.upper(data.get("player")) != "O":
            return self._response.send(
                data={
                    "msg": "Os dados enviados não estão no padrão veja na documentação e tente novamente!",
                    "errors": {
                        "player": ["must be required is in X or O"]
                    }
                },
                status=HTTPStatus.BAD_REQUEST,
            )

        return self.match.update_match_make_move(match_id=match_id, body=data)
