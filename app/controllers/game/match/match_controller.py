from http import HTTPStatus
from logzero import logger
import uuid
import random

from app.services.sqlalchemy.sqlalchemy import get_session
from app.utils.http.response.response import Response
from app.models.match_model import MatchModel
from app.helpers.winner_positions import POSITIONS_WINNERS
from app.helpers.rows_columns import ROWS, COLUMNS
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
                data={"id": match_id, "firstPlayer": next_player},
                status=HTTPStatus.OK,
            )
        except Exception as e:
            logger.info(f"Error create_match -> {str(e)}")
            return Response().send(
                data={"msg": "Não foi possivel realizar a jogada. Tente novamente mais tarde!"},
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    def __get_match(self, match_id: str):
        return self.session.query(MatchModel) \
            .filter(MatchModel.id == match_id) \
            .first()

    def __update_winner_match(self, match_id: str, winner: str):
        self.session.query(MatchModel).filter(
            MatchModel.id == match_id
        ).update(dict(winner=winner))
        self.session.commit()
        self.session.close()

    def __update_next_player_match(self, match_id: str, next_player: str):
        self.session.query(MatchModel).filter(
            MatchModel.id == match_id
        ).update(dict(next_player=next_player))
        self.session.commit()
        self.session.close()

    @staticmethod
    def __get_position_by_x_y(positions: list, body_position_x: int, body_position_y: int):
        for position in positions:
            if position.x == body_position_x and position.y == body_position_y:
                return position

        return None

    @staticmethod
    def __is_invalid_turn_of_player(next_player: str, player_body: str) -> bool:
        return next_player != player_body

    @staticmethod
    def __existing_owner_in_position(position) -> bool:
        return position.owner is not None

    @staticmethod
    def __validate_is_match_equal_draw(positions: list) -> bool:
        result = filter(lambda x: x.owner is not None, positions)
        return len(list(result)) == (ROWS * COLUMNS)

    def __validate_is_match_equal_winner(self, positions) -> str:
        list_owner_O = list(filter(lambda x: x.owner == "O", positions))
        list_owner_X = list(filter(lambda x: x.owner == "X", positions))

        if self.__check_victory(list_owner_X):
            return "X"

        if self.__check_victory(list_owner_O):
            return "O"

        return ""

    @staticmethod
    def __check_victory(positions) -> bool:
        for pos_win in POSITIONS_WINNERS:
            winn_cont = 0
            for position in pos_win:
                result = list(filter(lambda pos: pos.x == position.get("x") and pos.y == position.get("y"), positions))
                if len(result) > 0:
                    winn_cont += 1
            if winn_cont == 3:
                return True

        return False

    @staticmethod
    def __get_position_by_xy(positions, x, y):
        result = list(filter(lambda pos: pos.x == x and pos.y == y, positions))
        if len(result) == 0:
            return "-"

        if result[0].owner is None:
            return "-"

        return f"{result[0].owner}"

    def __render_graph_game(self, positions, next_player):
        get = self.__get_position_by_xy
        line1 = f"  {get(positions, 0, 2)} | {get(positions, 1, 2)} | {get(positions, 2, 2)}  "
        line2 = f"  {get(positions, 0, 1)} | {get(positions, 1, 1)} | {get(positions, 2, 1)}  "
        line3 = f"  {get(positions, 0, 0)} | {get(positions, 1, 0)} | {get(positions, 2, 0)}  "

        return {
            "1": line1,
            "2": line2,
            "3": line3,
            "4": "",
            "5": f"NextPlayer -> {next_player}"
        }

    def update_match_make_move(self, match_id: str, body: dict):
        try:
            match_by_id = self.__get_match(match_id)

            if match_by_id is None:
                return Response().send(
                    data={"msg": "Partida não encontrada"},
                    status=HTTPStatus.NOT_FOUND,
                )

            if match_by_id.winner:
                return Response().send(
                    data={"msg": "Partida finalizada", "winner": match_by_id.winner},
                    status=HTTPStatus.OK,
                )

            if self.__is_invalid_turn_of_player(match_by_id.next_player, str.upper(body.get("player"))):
                return Response().send(
                    data={"msg": "Não é turno do jogador"},
                    status=HTTPStatus.BAD_REQUEST,
                )

            position = self.__get_position_by_x_y(match_by_id.positions, body.get("position").get("x"),
                                                  body.get("position").get("y"))

            if position is None or self.__existing_owner_in_position(position):
                return Response().send(
                    data={"msg": "Essa posição já está preenchida ou não existe. Tente novamente!"},
                    status=HTTPStatus.BAD_REQUEST,
                )

            self.position.update_owner_position(position, str.upper(body.get("player")))

            positions_updated = self.position.get_all_position_by_mach_id(match_id)

            winner = self.__validate_is_match_equal_winner(positions_updated.all())
            if winner != "":
                self.__update_winner_match(match_id, winner)

                return Response().send(
                    data={"msg": "Partida finalizada", "winner": winner},
                    status=HTTPStatus.OK,
                )

            if self.__validate_is_match_equal_draw(positions_updated):
                return Response().send(
                    data={"msg": "Partida finalizada", "winner": "Draw"},
                    status=HTTPStatus.OK,
                )

            if match_by_id.next_player == "X":
                next_player = "O"
            else:
                next_player = "X"

            self.__update_next_player_match(match_id, next_player)

            return Response().send(
                data=self.__render_graph_game(positions_updated, next_player),
                status=HTTPStatus.OK,
            )
        except Exception as e:
            logger.info(f"Error make a move -> {str(e)}")
            return Response().send(
                data={"msg": "Não foi possivel realizar a jogada. Tente novamente mais tarde!"},
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
            )
