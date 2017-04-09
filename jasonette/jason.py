from flask import Flask
app = Flask(__name__)

@app.route("/cards")
def cards():
  with open('cards.json', 'r') as f:
    data = f.read()

  return data

@app.route("/card")
def card():
  with open('card.json', 'r') as f:
    data = f.read()

  return data

@app.route("/corporations")
def corporations():
  with open('corporations.json', 'r') as f:
    data = f.read()

  return data

@app.route("/accounts")
def accounts():
  with open('accounts.json', 'r') as f:
    data = f.read()

  return data

@app.route("/new_card")
def new_card():
  with open('new_card.json', 'r') as f:
    data = f.read()

  return data


if __name__ == "__main__":
  app.run(port=8000)