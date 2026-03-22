from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello {name}, 5000 kottara LOVDAY!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
