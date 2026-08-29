from flask import Flask

from config.settings import (
    APP_HOST,
    APP_PORT,
    APP_ENV,
)

from api.data_routes import data_bp


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)

    # Register API routes
    app.register_blueprint(data_bp)

    @app.get("/")
    def health_check():
        return {
            "status": "ok",
            "service": "Retail Intelligence Copilot",
            "environment": APP_ENV
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host=APP_HOST,
        port=APP_PORT,
        debug=(APP_ENV == "development")
    )