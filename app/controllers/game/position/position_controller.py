import uuid

from app.services.sqlalchemy.sqlalchemy import get_session
from app.models.position_model import PositionModel
from app.utils.http.response.response import Response
from app.helpers.rows_columns import COLUMNS, ROWS
from logzero import logger


class PositionController:
    def __init__(self, **args):
        self.session = get_session()
        self.match_id = args.get("match_id")

    def create_positions_to_match(self, match_id: str):
        try:
            for positionX in range(0, COLUMNS):
                for positionY in range(0, ROWS):
                    position_id = str(uuid.uuid4())
                    model = PositionModel(id=position_id, match_id=match_id, x=positionX, y=positionY)
                    self.session.add(model)

            self.session.commit()
            self.session.close()
        except Exception as e:
            logger.info(f"Error create_position_to_match -> {str(e)}")
            raise e

    def update_position(self):
        return

    def get_one_position(self):
        return

    def get_all_position_by_mach(self):
        return
