import unittest
from flask_restplus import fields

from app.services.restplus.restplus import api
from app.utils.restplus.restplus import response_serializer


class TestResponseSerializer(unittest.TestCase):
    def test_should_serializer_object_to_model_and_return_name_default(self):
        data = {
            "id": fields.String(required=True),
            "firstPlayer": fields.String(required=True),
        }
        model = api.model("Match", data)
        response = response_serializer(model)
        self.assertIsNotNone(response)
        self.assertEqual(response.name, "Response")


if __name__ == '__main__':
    unittest.main()
