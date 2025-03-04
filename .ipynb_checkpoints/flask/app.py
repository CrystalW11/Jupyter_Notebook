from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/data", methods=["GET"])
def get_data():
    # You can modify this to return more complex data
    response = {"message": "Hello from Python!"}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
