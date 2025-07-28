#!/usr/bin/env python3
"""
Example file with various security vulnerabilities for testing the AI scanner.
This file is intentionally vulnerable and should only be used for testing purposes.
"""

import os
import subprocess
import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded secrets (vulnerability)
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "my-super-secret-token"

def vulnerable_sql_injection(user_input):
    """Vulnerable function with SQL injection."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    
    # Another SQL injection
    query2 = "SELECT * FROM users WHERE id = " + user_input
    cursor.execute(query2)
    
    return cursor.fetchall()

def vulnerable_command_injection(command):
    """Vulnerable function with command injection."""
    # Command injection vulnerability
    os.system(command)
    
    # Another command injection
    subprocess.run(command, shell=True)
    
    # More command injection
    result = subprocess.check_output(command, shell=True)
    return result

def vulnerable_xss(user_input):
    """Vulnerable function with XSS."""
    # XSS vulnerability
    html = f"<div>Welcome, {user_input}!</div>"
    
    # Another XSS
    template = f"""
    <html>
        <head><title>User Profile</title></head>
        <body>
            <h1>Hello {user_input}</h1>
            <p>Your profile: {user_input}</p>
        </body>
    </html>
    """
    
    return render_template_string(template)

def vulnerable_path_traversal(filename):
    """Vulnerable function with path traversal."""
    # Path traversal vulnerability
    file_path = "/var/www/uploads/" + filename
    with open(file_path, 'r') as f:
        return f.read()

def vulnerable_deserialization(data):
    """Vulnerable function with insecure deserialization."""
    import pickle
    
    # Insecure deserialization
    obj = pickle.loads(data)
    return obj

def vulnerable_authentication(username, password):
    """Vulnerable authentication function."""
    # Hardcoded credentials (vulnerability)
    if username == "admin" and password == "admin123":
        return True
    
    # Weak password check
    if password == "password":
        return True
    
    return False

def vulnerable_file_upload(file):
    """Vulnerable file upload function."""
    # Insecure file upload
    filename = file.filename
    file.save(f"/uploads/{filename}")
    
    # No validation of file type or content
    return f"File {filename} uploaded successfully"

def vulnerable_logging(user_input):
    """Vulnerable logging function."""
    # Insecure logging - logs sensitive data
    print(f"User input: {user_input}")
    print(f"Password: {DATABASE_PASSWORD}")
    print(f"API Key: {API_KEY}")

def vulnerable_eval_usage(user_input):
    """Vulnerable function using eval."""
    # Dangerous eval usage
    result = eval(user_input)
    return result

def vulnerable_redirect(url):
    """Vulnerable redirect function."""
    # Open redirect vulnerability
    return f"<script>window.location.href='{url}';</script>"

@app.route('/login', methods=['POST'])
def login():
    """Vulnerable login endpoint."""
    username = request.form.get('username')
    password = request.form.get('password')
    
    # SQL injection in login
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    # XSS in response
    if vulnerable_authentication(username, password):
        return f"<h1>Welcome {username}!</h1>"
    else:
        return "<h1>Login failed</h1>"

@app.route('/search')
def search():
    """Vulnerable search endpoint."""
    query = request.args.get('q', '')
    
    # SQL injection
    results = vulnerable_sql_injection(query)
    
    # XSS in response
    return f"<div>Search results for: {query}</div>"

@app.route('/execute')
def execute():
    """Vulnerable command execution endpoint."""
    command = request.args.get('cmd', '')
    
    # Command injection
    result = vulnerable_command_injection(command)
    
    return f"Command output: {result}"

@app.route('/profile/<username>')
def profile(username):
    """Vulnerable profile endpoint."""
    # XSS vulnerability
    return f"""
    <html>
        <head><title>Profile</title></head>
        <body>
            <h1>Profile for {username}</h1>
            <p>Username: {username}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Insecure configuration
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    # More vulnerabilities
    user_input = input("Enter command: ")
    vulnerable_eval_usage(user_input)
    
    # Insecure file operations
    filename = input("Enter filename: ")
hjS
    vulnerable_path_traversal(filename) 
