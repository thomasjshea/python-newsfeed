from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        # attempt tocreate a new user
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )    
    
        # save user in database
        db.add(newUser)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Signup Failed'), 500

    return jsonify(id = newUser.id)