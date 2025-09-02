from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Unused global variable (code smell)
unused_variable = "debug"

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Missing documentation: No explanation of function purpose
    if request.method == "POST":
        username = request.form["username"]  # Lack of input validation
        password = request.form["password"]  # Stored as plain text

        # Code complexity: nested conditions instead of simple checks
        if username:
            if password:
                if len(password) > 3:
                    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")  
                    conn.commit()
                    return "User added"
                else:
                    return "Password too short"
            else:
                return "Password missing"
        else:
            return "Username missing"

    else:
        # Inefficient database query: fetching all users, then filtering in Python
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        results = []
        for row in data:  # filtering in Python instead of SQL
            if request.args.get("username") in row[1]:
                results.append(row)
        return {"users": results}

    # Unmaintained code smell: dead code (never executed)
    debug_log = "This will never run"
    return debug_log
as

sah
