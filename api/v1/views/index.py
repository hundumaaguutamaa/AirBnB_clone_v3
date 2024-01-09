#!/usr/bin/python3
""" Returning a Json response. """

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/api/v1/stats', methods=['GET'])
def object_stats():
    """ Use the count() method from storage to retrieve
        the number of objects by type
    """

    objects = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User'),
            }
    return jsonify(objects)
