from flask import url_for
from flask_restplus import Api

import settings

_config = settings.load_config()
_doc = "/docs"
if _config.SWAGGER_VISIBLE in ("false", "False", False):
    _doc = False


class MyApi(Api):
    @property
    def specs_url(self):
        """
        The Swagger specifications absolute url (ie. `swagger.json`)
        :rtype: str
        """

        return url_for(self.endpoint("specs"), _external=False)


api = MyApi(
    version="1.0",
    title=_config.SWAGGER_TITLE,
    description=_config.SWAGGER_DESCRIPTION,
    doc=_doc,
    ordered=True,
    catch_all_404s=True
)


def configuration_restplus(app, blueprint):
    api.init_app(blueprint)
    app.register_blueprint(blueprint)
    app.api = api
