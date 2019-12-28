import unittest
import bson
import uuid
from flask import Flask

from app.utils.http.response.response import Response


class TestResponse(unittest.TestCase):
    def test_should_send_dict_data_and_return_status_code_expected(self):
        app = Flask(__name__)
        with app.test_request_context():
            data = {"objectid": str(bson.objectid.ObjectId()), "uuid": str(uuid.uuid4())}
            response = Response().send(data=data, status=200)
            print(response)
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
