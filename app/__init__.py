# Import necessary modules
from flask import Flask
from .routes.ocr_routes import ocr_blueprint

def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Register OCR blueprint (routes)
    app.register_blueprint(ocr_blueprint, url_prefix='/api/v1/ocr')

    return app
