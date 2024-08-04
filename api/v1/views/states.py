#!/usr/bin/python3
"""States API"""

from api.v1.views import app_views
from flask import abort, jsonify
from models import storage
from models.state import State

def err_404(e):
    """Page not found"""
    if not e:
        abort(404)

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_states():
    """Retrieve states"""
    return jsonify([state.to_dict() for state
                   in storage.all(State).values()]), 200

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state_id(state_id):
    """Retrieve state Using state ID"""
    data = storage.get(State, state_id)
    #err_404(data)
    return jsonify(data.to_dict()), 200
