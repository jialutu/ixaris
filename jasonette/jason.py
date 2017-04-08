from flask import Flask
app = Flask(__name__)

@app.route("/cards")
def cards():
  with open('cards.json', 'r') as f:
    data = f.read()

  return data

@app.route("/corporations")
def corporations():
  with open('corporations.json', 'r') as f:
    data = f.read()

  return data

if __name__ == "__main__":
  app.run(port=8000)