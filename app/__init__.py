from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object("config.Config")

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


