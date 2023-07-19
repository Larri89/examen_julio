from flask import Flask, request, jsonify
import logging
from repository import InMemoryRepository

app = Flask(__name__)

repository = InMemoryRepository()

@app.route('/create/user/<int:user_id>/<str:user_name>/<int:user_age>', methods=['POST'], endpoint='create_user')
def create_user(user_id, user_name, user_age):
    repository.add({'id': user_id, 'name': '%s', 'age': user_age}) % (user_name)

@app.route('/user/<int:user_id>', methods=['GET'], endpoint='get_user')
def get_user(user_id):
    print(repository.get(user_id))

if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000)