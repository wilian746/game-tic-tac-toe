from http import HTTPStatus

from datetime import date

from app.services.sqlalchemy.sqlalchemy import get_session
from app.models.match_model import MatchModel
from app.utils.http.response.response import Response

class GameHandler:
    def __init__(self):
        self._response = Response()

    @staticmethod
    def create_match():
        session = get_session()
        bruno = MatchModel("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
        john = MatchModel("John Doe", date(1990, 5, 17), 173, 90)
        session.add(bruno)
        session.add(john)
        session.commit()
        session.close()
        return Response().send(
            data=None,
            status=HTTPStatus.OK,
        )


    def make_move(self, _id: str):
        return Response().send(
            data=_id,
            status=HTTPStatus.OK,
        )
