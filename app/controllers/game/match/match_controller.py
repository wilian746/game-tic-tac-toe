from http import HTTPStatus

from app import db
from app.utils.http.response.response import Response

# import random
# random.choice(["X", "O"])


class MatchController:
    def __init__(self):
        self._response = Response()

    def create_match(self, data):
        try:
            db.session.add(data)
            db.session.commit()

            return self._response.send(
                data=data, status=HTTPStatus.CREATED
            )
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
    def get_match(self):
        return

    def get_all_match(self):
        return

    def update_match_make_move(self):
        return
