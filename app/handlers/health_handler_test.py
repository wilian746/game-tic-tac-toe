import unittest
from flask import Flask

from app.handlers.health_handler import HealthHandler


class TestHealthHandler(unittest.TestCase):
    def test_should_check_health_and_return_status_code_200(self):
        app = Flask(__name__)
        with app.test_request_context():
            response = HealthHandler().get()
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
