#!/usr/bin/python3
""" create a Flask application. """

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

# Flask application instance app
app = Flask(__name__)

# Register a blueprint app_views to the Flask instance app
app.register_blueprint(app_views)

# Declare a method to handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

if __name__ == "__main__":
    # Run the Flask server with specified host and port
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

