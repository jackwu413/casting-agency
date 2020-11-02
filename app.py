import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  return app

app = create_app()


@app.route('/')
def home(): 
  return "Hello World"

@app.route('/actors', methods=['GET'])
def get_actors(): 
  actors = Actor.query.all()
  return jsonify({
    'success': True, 
    'actors': actors
  }), 200


#Dcoument how to make post request: http://0.0.0.0/actors?name=<string:name>&age=<int:age>&gender=<string:gender>
@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def add_actor(payload):
  name = request.args.get('name')
  age = request.args.get('age')
  gender = request.args.get('gender')

  try: 
    actor = Actor(
      name = name, 
      age = age, 
      gender = gender 
    )
    actor.insert()
  except: 
    abort(400)

  return jsonify({
    'success': True, 
    'actor': actor
  }), 200






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
