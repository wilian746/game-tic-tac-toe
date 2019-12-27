from flask import Blueprint, render_template
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.middleware.proxy_fix import ProxyFix

from app.middlewares.request_middleware import config_middlewares
from app.middlewares.error_handlers_middleware import config_error_handlers
from app.models import import_model_files
from app.services.restplus import configuration_restplus
from app.routes import import_route_files
from app.services.sqlalchemy import initialize_database
from settings import load_config


# Initialize Flask
app = Flask(__name__, static_folder="static")
app.url_map.strict_slashes = False
blueprint = Blueprint("api", __name__, url_prefix=None)

# handle home screen to redirect to the documentation
@app.route("/", methods=['GET'])
def home_handler():
    return "<html style='width: 100%; height: 100%; margin: 0; padding: 0;'>" \
             "<body style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; flex-direction: column; margin: 0; padding: 0; background-image: url(\"https://thumbs.gfycat.com/WelcomeConcreteHellbender-small.gif\"); background-repeat: no-repeat; background-position: top;'>" \
               "<h1 style='display: block; line-height: 36px; height: 36px; width: 100%; font-size: 30px; text-align: center; text-transform: uppercase; color: #00009C; margin: 70px 0;background-color:#fff;'>" \
                 "Bem vindo!" \
               "</h1>" \
               "<h3 style='display: block; line-height: 30px; height: 30px; width: 100%;background-color:#fff'>" \
                 "<a href='/docs' style='display: block; line-height: 30px; height: 30px; width: 100%; font-size: 24px; text-align: center; text-transform: uppercase; color: #4343ff;'>" \
                    "Clique aqui para ser redirecionado para a documentação" \
                 "</a>" \
               "</h3>" \
               "<footer style='position: fixed; bottom: 0; right: 0; width: 100px; height: 100px; background-image: url(\"https://e3ba6e8732e83984.cdn.gocache.net/uploads/image/file/973314/regular_ea93c3589225d4cf45fed1909e81a53f.png\"); background-repeat: no-repeat; background-size: 100px;'></footer>" \
               "</body>" \
           "</html>"

# Proxy
app.wsgi_app = ProxyFix(app.wsgi_app)


# Configuration Cors
CORS(app, resources={r"/*": {"origins": "*"}})


# Load configuration
app.config.from_object(load_config())


# Initialize SQL Alchemy and import models
db = initialize_database(load_config())
app.db = db
app.sqlAlchemy = SQLAlchemy()
import_model_files()


# Initialize Marshmallow
marshmallow = Marshmallow()
marshmallow.init_app(app)
app.marshmallow = Marshmallow()


# Initialize Restplus and import Routes
configuration_restplus(app=app, blueprint=blueprint)
import_route_files()


# Configuration Middlewares and Error Handlers
config_middlewares(app=app)
config_error_handlers(app=app)
