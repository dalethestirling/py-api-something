from flask import Flask
app = Flask(__name__)

@app.route("/api/v1/something")
def something():
    return "{ value: \"something\" }"

if __name__ == "__main__":
    app.run(
      host='0.0.0.0',
      port=5001
      )
