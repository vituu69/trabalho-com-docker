from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_word():
    return 'ola estou na aplicacao setada'

# app.run(debug=True) 