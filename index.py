from flask import Flask

app = Flask(__name__)

PORT=5000

@app.route("/")
def hello():
  return "Hello, World!"

@app.route("/hi")
def hello_again():
  return "Hello, World 2!"

if __name__ == '__main__':
  app.run(port=PORT)
