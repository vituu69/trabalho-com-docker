from flask import Flask, request
from .src.init import User_repo
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_word():
    return 'ola estou na aplicacao setada'

@app.route("/insert", methods=["POST"])
def insert():
    user_repo = User_repo()
    body = request.json

    user_repo.insert_name(body['name'])

    return 'ok'

if __name__ == "__main__":
    app.run(debug=True)