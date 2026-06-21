from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
next_id = 1

@app.route("/")
def home():
    return jsonify({"message": "Todo API is running", "status": "ok"})

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    global next_id
    data = request.get_json()
    todo = {"id": next_id, "task": data.get("task"), "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
