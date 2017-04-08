from flask import Flask
from main import *
app = Flask(__name__)

@app.route("/auth/<username>/<password>")
def auth(username, password):
  token = get_token(credentialCode=username, password=password)
  return str(token)

@app.route("/corporations")
def corporations():
  return str(get_corporations())

@app.route("/accounts")
def accounts():
  return str(get_accounts())

@app.route("/cards")
def cards():
  return str(get_cards()).replace("'", '"')

if __name__ == "__main__":
  app.run()