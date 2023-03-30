from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
csrf = CSRFProtect()
login_context = LoginManager()


def create_app():
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")

    # Initialize Plugins
    db.init_app(app)
    csrf.init_app(app)
    login_context.init_app(app)

    @login_context.user_loader
    def load_user(user_id):
        from app.models import User

        return User.query.get(int(user_id))

    with app.app_context():
        from . import paths
        from . import auth

        app.register_blueprint(paths.home_bp)
        app.register_blueprint(auth.auth_bp)

    return app
