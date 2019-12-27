from app.controllers.game.match.match_controller import MatchController
from app.utils.http.response.response import Response
from http import HTTPStatus
from flask import request
from app.schemas.models.make_move import MakeMoveSchema
from app import app

class GameHandler:
    def __init__(self):
        self._controller = MatchController()
        self._response = Response()

    def create_match(self):
        try:
            return self._response.send(
                data=None,
                status=200,
            )
        except Exception as e:
            return self._response.send(
                data=str(e), status=500
            )

    def make_move(self, _id: str):
        body = request.get_json(silent=True, force=True)
        data, errors = MakeMoveSchema(app.marshmallow.ModelSchema).load(data=body)
        if errors:
            return self._response.send(
                data=errors,
                status=HTTPStatus.BAD_REQUEST,
            )

        return self._response.send(
            data=data,
            status=200,
        )
