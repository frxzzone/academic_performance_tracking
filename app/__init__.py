"""Application factory."""
from pathlib import Path

from flask import Flask, jsonify

from config import Config
from .extensions import db


def create_app(config_object=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    db.init_app(app)

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    @app.get("/health")
    def health():
        return jsonify(status="ok", application="Academic Performance Tracking")

    return app
