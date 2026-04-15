from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# --- Database Setup (Executes on startup) ---
def init_db():
    conn = sqlite3.connect('mit_events.db')
    cursor = conn.cursor()
    # Table to store event registrations
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
         student_name TEXT, student_email TEXT, event_type TEXT, sub_event TEXT, 
         timestamp TEXT)''')
    conn.commit()
    conn.close()

# Ensure the database and table exist before the app starts
init_db()

@app.route('/')
def index():
    # Serves the HTML file from the 'templates' folder
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        # Simple backend validation
        if not data['name'] or not data['email']:
            return jsonify({"status": "error", "message": "Name and email are mandatory!"})

        conn = sqlite3.connect('mit_events.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registrations (student_name, student_email, event_type, sub_event, timestamp) VALUES (?,?,?,?,?)",
                       (data['name'], data['email'], data['event_type'], data['sub_event'], datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Registration received at MIT CSN!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    # Starts the local development server (http://127.0.0.1:5000)
    app.run(debug=True)