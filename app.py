from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Learn Kubernetes"}
    ]
@app.route("/")
def home():
    return "DevOps Learning Project v2"
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"]
    }
    tasks.append(new_task)
    return jsonify(new_task), 201
@app.route("/health")
def health():
    return {"status": "healthy"}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
