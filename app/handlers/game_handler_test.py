import unittest
import json
from flask import Flask
from app.handlers.game_handler import GameHandler


class TestResponse(unittest.TestCase):
    def test_should_create_match_and_return_status_code_200(self):
        app = Flask(__name__)
        with app.test_request_context():
            response = GameHandler().create_match()
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.json)
            self.assertTrue(len(response.json.get("id")) > 0)
            self.assertIn(response.json.get("firstPlayer"), ["X", "O"])

    def test_should_make_move_and_return_status_code_400_body_incorrect(self):
        app = Flask(__name__)
        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            response = GameHandler().make_move(response_create_match.json.get("id"))
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 400)

    def test_should_make_move_and_return_status_code_400_player_type_incorrect(self):
        app = Flask(__name__)
        body = {
            "id": "",
            "player": "z",
            "position": {"x": 1, "y": 1}
        }

        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            body["id"] = response_create_match.json.get("id")

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 400)

    def test_should_make_move_and_return_status_code_200(self):
        app = Flask(__name__)
        body = {
            "id": "",
            "player": "x",
            "position": {"x": 1, "y": 1}
        }

        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            body["id"] = response_create_match.json.get("id")
            body["player"] = response_create_match.json.get("firstPlayer")

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)

    def test_should_make_move_and_return_status_code_404_match_not_found(self):
        app = Flask(__name__)
        body = {
            "id": "111111",
            "player": "x",
            "position": {"x": 1, "y": 1}
        }

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 404)

    def test_should_make_move_and_return_status_code_400_position_owner_existing(self):
        app = Flask(__name__)
        body = {
            "id": "",
            "player": "x",
            "position": {"x": 1, "y": 1}
        }

        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            body["id"] = response_create_match.json.get("id")
            body["player"] = response_create_match.json.get("firstPlayer")

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)
            if body["player"] == "X":
                body["player"] = "O"
            else:
                body["player"] = "X"
            response_error = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response_error)
            self.assertEqual(response_error.status_code, 400)

    def test_should_make_move_and_return_status_code_400_position_owner_existing(self):
        app = Flask(__name__)
        body = {
            "id": "",
            "player": "x",
            "position": {"x": 1, "y": 1}
        }

        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            body["id"] = response_create_match.json.get("id")
            body["player"] = response_create_match.json.get("firstPlayer")

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)
            if body["player"] == "X":
                body["player"] = "O"
            else:
                body["player"] = "X"
            response_error = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response_error)
            self.assertEqual(response_error.status_code, 400)

    def test_should_make_move_and_return_status_code_400_not_your_turn(self):
        app = Flask(__name__)
        body = {
            "id": "",
            "player": "x",
            "position": {"x": 1, "y": 1}
        }

        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            body["id"] = response_create_match.json.get("id")
            body["player"] = response_create_match.json.get("firstPlayer")

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)
            body["position"]["x"] = 0
            response_error = GameHandler().make_move(body["id"])
            self.assertIsNotNone(response_error)
            self.assertEqual(response_error.status_code, 400)

    def test_should_make_move_and_return_status_code_200_with_winner_or_draw(self):
        app = Flask(__name__)
        body = {
            "id": "",
            "player": "X",
            "position": {"x": 0, "y": 0}
        }

        with app.test_request_context():
            response_create_match = GameHandler().create_match()
            body["id"] = response_create_match.json.get("id")
            body["player"] = response_create_match.json.get("firstPlayer")
            if body["player"] == "O":
                body["position"] = {"x": 1, "y": 0}

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)

        if body["player"] == "O":
            body = change_player_and_set_position(body, 0, 0)
        else:
            body = change_player_and_set_position(body, 1, 0)

        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)

        body = change_player_and_set_position(body, 2, 0)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])

        body = change_player_and_set_position(body, 0, 1)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])

        body = change_player_and_set_position(body, 1, 1)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])

        body = change_player_and_set_position(body, 2, 1)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])

        body = change_player_and_set_position(body, 0, 2)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])

        body = change_player_and_set_position(body, 1, 2)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])

        body = change_player_and_set_position(body, 2, 2)
        with app.test_request_context(data=json.dumps(body)):
            response = GameHandler().make_move(body["id"])
            self.assertEqual(response.status_code, 200)
            if response.json.get("winner"):
                self.assertIn(response.json.get("winner"), ["X", "O", "Draw"])


def change_player_and_set_position(body: dict, x: int, y: int) -> dict:
    if body["player"] == "O":
        body["player"] = "X"
    else:
        body["player"] = "O"

    body["position"] = {"x": x, "y": y}
    return body


if __name__ == '__main__':
    unittest.main()
