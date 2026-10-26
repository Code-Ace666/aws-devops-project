from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Hello, Flask!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify(error="'name' is required"), 400
    return jsonify(message=f"Hello, {name}!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
