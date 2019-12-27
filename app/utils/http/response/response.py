import json
from datetime import datetime
from uuid import UUID
from bson import ObjectId

from flask import make_response


class Response:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def send(
        self,
        data=None,
        status=200,
        headers=None,
    ):
        response = {}
        if status not in [204]:
            data = json.dumps(data, default=self.__format_encoder_object)
            data = json.loads(data)

            response = data

        headers = self.__format_headers(headers)
        return make_response(json.dumps(response), status, headers)

    def __format_headers(self, headers=None) -> dict:
        if headers is None:
            headers = {}

        try:
            for key, value in self.headers.items():
                if key.lower() not in list(map(str.lower, headers.keys())):
                    headers[key] = value
        except Exception:
            headers = self.headers
        finally:
            return headers

    def __format_encoder_object(o):
        if type(o) == ObjectId:
            return str(o)
        elif type(o) == datetime:
            return o.isoformat()
        elif type(o) == UUID:
            return str(o)
        return o.__str__
