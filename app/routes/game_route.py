from flask_restplus import Resource

from app.handlers.game_handler import GameHandler
from app.schemas.routes.game_schema import GameSchema
from app.services.restplus.restplus import api

ns = api.namespace(
    path="/game",
    name="Game",
    description="Start or Make a move of TicTacToe"
)

schema = GameSchema()

@ns.route("")
@api.response(code=200, description="ok")
@api.response(code=400, description="bad_request")
@api.response(code=500, description="internal_error")
class GameCreateMatch(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler = GameHandler().create_match

    @api.response(code=200, model=schema.response_match, description="match room created")
    def post(self):
        """
        Create match
        """
        return self.handler()


parser_id = api.parser()
parser_id.add_argument(
    "id",
    type=str,
    help="Game identifier of type UUID",
    location="path",
    required=True,
)


@ns.route("/<id>/movement")
@api.expect(parser_id)
@api.response(code=200, description="ok")
@api.response(code=201, description="created")
@api.response(code=400, description="bad_request")
@api.response(code=404, description="not_found")
@api.response(code=409, description="conflict")
@api.response(code=500, description="internal_error")
class GameMakeMove(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler = GameHandler().make_move

    @api.response(code=200, model=schema.response_status_winner, description="make move return draw")
    @api.response(code=201, model=schema.response_winner, description="make move return winner")
    @api.response(code=400, model=schema.response_msg, description="make move return not your turn or already exist winner in match")
    @api.response(code=404, model=schema.response_msg, description="make move return match not found")
    @api.response(code=409, model=schema.response_msg, description="make move return position not allowed or with owner existing in position selected")
    @api.doc(security=False, body=schema.response_make_move)
    def post(self, id):
        """
        Make a move in match
        """
        return self.handler(id)

