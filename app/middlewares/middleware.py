from http import HTTPStatus

from flask import request
from app.utils.http.response.response import Response


def config_middlewares(app):
    @app.before_request
    def before_request():
        if request.method in ("POST", "PUT"):
            body = request.get_json(silent=True, force=True)
            if not body:
                return Response().send(
                    status=HTTPStatus.BAD_REQUEST,
                    message="The request body must be informed",
                    code="body_not_informed",
                )

    @app.after_request
    def after_request(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Cache-Control"] = "no-store"
        response.headers["Pragma"] = "no-cache"
        response.headers["Server"] = "no-server"
        return response
