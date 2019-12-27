from http import HTTPStatus
from logzero import logger
import uuid
import random

from app.services.sqlalchemy.sqlalchemy import get_session
from app.utils.http.response.response import Response
from app.models.match_model import MatchModel
from app.controllers.game.position.position_controller import PositionController


class MatchController:
    def __init__(self):
        self.position = PositionController()
        self._response = Response()
        self.session = get_session()

    def create_match(self):
        try:
            match_id = str(uuid.uuid4())
            next_player = random.choice(["X", "O"])
            model = MatchModel(id=match_id, next_player=next_player)
            self.session.add(model)
            self.session.commit()
            self.session.close()

            self.position.create_positions_to_match(match_id)

            return Response().send(
                data={
                    "id": match_id,
                    "firstPlayer": next_player
                },
                status=HTTPStatus.OK,
            )
        except Exception as e:
            logger.info(f"Error create_match -> {str(e)}")
            return Response().send(
                data={
                    "msg": "Não foi possivel realizar a jogada. Tente novamente mais tarde!"
                },
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    def get_match(self):
        return

    def get_all_match(self):
        return

    def update_match_make_move(self):
        return
