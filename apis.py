from flask import Flask
from main import *
app = Flask(__name__)

@app.route("/<username>/<password>")
def auth(username, password):
  token = get_token(credentialCode=username, password=password)
  return str(token)

@app.route("")

if __name__ == "__main__":
  app.run()