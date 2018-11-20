import time
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/posts", methods=["POST"])
def posts():

  # Get start and end point for posts to generate
  start = int(request.form.get("start") or 0)
  end = int(request.form.get("end") or (start + 9))

  # Generate list of post
  data = []
  for i in range(start, end +1):
    data.append(f"Post #{i}")

  # Artificially delay speed of response
  time.sleep(1)

  # Return list of post
  return jsonify(data)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)