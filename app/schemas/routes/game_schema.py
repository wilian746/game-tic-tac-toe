from flask_restplus import fields
from app.services.restplus import api

from app.utils.restplus.restplus import response_serializer


class GameSchema:
    @property
    def _obj_match_move(self):
        return {
            "id": fields.String(required=True),
            "next_player": fields.String(required=True),
        }

    @property
    def match(self):
        return api.model("Match", self._obj_match_move)

    @property
    def response_match(self):
        return response_serializer(data=self.match, name_model="Match_Response")

    @property
    def make_move(self):
        return api.model("Make_Move", self._obj_make_move)

    @property
    def position(self):
        return api.model("Position", self._obj_position)

    @property
    def _obj_position(self):
        return {
            "x": fields.String(required=True),
            "y": fields.String(required=True)
        }

    @property
    def response_position(self):
        return response_serializer(data=self.position, name_model="Position_Response")

    @property
    def _obj_make_move(self):
        return {
            "id": fields.String(required=True),
            "player": fields.String(required=True),
            "position": fields.Nested(self.position, required=True)
        }

    @property
    def response_make_move(self):
        return response_serializer(data=self.make_move, name_model="Make_Move_Response")


    @property
    def _obj_msg(self):
        return {
            "msg": fields.String(required=True),
        }

    @property
    def msg(self):
        return api.model("Msg", self._obj_msg)

    @property
    def response_msg(self):
        return response_serializer(data=self.msg, name_model="Msg_Response")

    @property
    def _obj_winner(self):
        return {
            "msg": fields.String(required=True),
            "winner": fields.String(required=True),
        }

    @property
    def winner(self):
        return api.model("Winner", self._obj_winner)

    @property
    def response_winner(self):
        return response_serializer(data=self.winner, name_model="Winner_Response")

    @property
    def _obj_status_winner(self):
        return {
            "status": fields.String(required=True),
            "winner": fields.String(required=True),
        }

    @property
    def status_winner(self):
        return api.model("Status_Winner", self._obj_status_winner)

    @property
    def response_status_winner(self):
        return response_serializer(data=self.status_winner, name_model="Status_Winner_Response")
