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

# Initialize CORS with the app instance
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Declare a method to handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """ Handler for 404 Not found errors. """
    return {'error': 'Not found'}, 404

if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
   
    app.run(host=host, port=port, threaded=True)
