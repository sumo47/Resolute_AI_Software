from flask import Flask
from .config import config
from .routes.auth_routes import auth_bp
from .routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")

    @app.route("/")
    def index():
        return "Welcome to the Flask Authentication System!"
    
    return app

app = create_app()
