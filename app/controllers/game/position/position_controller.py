from app import app


class PositionController:
    def __init__(self, **args):
        self.db = app.db
        self.match_id = args.get("match_id")

    def create_positions_to_match(self):
        return

    def update_position(self):
        return

    def get_one_position(self):
        return

    def get_all_position_by_mach(self):
        return
