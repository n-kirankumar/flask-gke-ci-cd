from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({
        "status": "ok",
        "service": "flask-gke-ci-cd"
    })

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from CI/CD pipeline"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  #nosec B104

