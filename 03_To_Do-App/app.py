from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Create DB
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            desc TEXT,
            cat TEXT,
            date TEXT,
            reminder TEXT,
            priority TEXT,
            done BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# GET tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    conn.close()

    tasks = []
    for r in rows:
        tasks.append({
            "id": r[0],
            "name": r[1],
            "desc": r[2],
            "cat": r[3],
            "date": r[4],
            "reminder": r[5],
            "priority": r[6],
            "done": bool(r[7])
        })
    return jsonify(tasks)

# ADD task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['id'],
        data['name'],
        data['desc'],
        data['cat'],
        data['date'],
        data['reminder'],
        data['priority'],
        data['done']
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task saved"})

# DELETE task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})

@app.route('/')
def home():
    return "Taskr Backend is Live 🚀"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)