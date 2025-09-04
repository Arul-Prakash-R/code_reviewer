import flask
import os
import subprocess
import pickle
import yaml
import xml.etree.ElementTree as ET
import re
import jwt
import requests
import socket
import threading
import time
import random
import sqlite3
from flask import Flask, request, redirect, render_template_string, make_response, session
from flask_cors import CORS
from cryptography.fernet import Fernet
import logging
import tempfile
import shutil
import ftplib
import http.client
import base64
import json
import html

app = Flask(__name__)

app.secret_key = "super_secret_key_123"
API_KEY = "my_hardcoded_api_key"
PASSWORD = "admin123"

app.config['DEBUG'] = True

CORS(app, resources={r"/*": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)

unused_var = 42

def dead_function():
    print("This is never called")
    pass

def CalculateTotal(Amount):
    return Amount + 10

def undocumented_function(a, b):
    return a + b

def complex_function(x):
    if x > 0:
        if x < 10:
            if x % 2 == 0:
                return "Even small positive"
            else:
                return "Odd small positive"
        else:
            if x % 2 == 0:
                return "Even large positive"
            else:
                return "Odd large positive"
    else:
        if x > -10:
            if x % 2 == 0:
                return "Even small negative"
            else:
                return "Odd small negative"
        else:
            if x % 2 == 0:
                return "Even large negative"
            else:
                return "Odd large negative"

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
cursor.execute("INSERT INTO users VALUES (1, 'admin', 'password')")
conn.commit()

def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['input']
        return f"You entered: {user_input}"
    return '''
        <form method="post">
            <input type="text" name="input">
            <input type="submit">
        </form>
    '''

@app.route('/sql_injection')
def sql_injection():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    try:
        cursor.execute(query)
        return str(cursor.fetchall())
    except Exception as e:
        return str(e)

@app.route('/command_injection')
def command_injection():
    cmd = request.args.get('cmd')
    output = subprocess.getoutput(cmd)
    return output

@app.route('/path_traversal')
def path_traversal():
    filename = request.args.get('file')
    with open(filename, 'r') as f:
        return f.read()

@app.route('/insecure_deserialization')
def insecure_deserialization():
    data = request.args.get('data')
    obj = pickle.loads(base64.b64decode(data))
    return str(obj)

@app.route('/eval_exec')
def eval_exec():
    code = request.args.get('code')
    result = eval(code)
    return str(result)

@app.route('/ssti')
def ssti():
    template = request.args.get('template')
    return render_template_string(template)

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    file.save(file.filename)
    return "File uploaded"

@app.route('/file_deletion')
def file_deletion():
    filename = request.args.get('file')
    os.remove(filename)
    return "File deleted"

@app.route('/lfi')
def lfi():
    file = request.args.get('file')
    with open(file, 'r') as f:
        return f.read()

@app.route('/output_encoding')
def output_encoding():
    user_input = request.args.get('input')
    return user_input

@app.route('/insecure_api')
def insecure_api():
    url = request.args.get('url')
    response = requests.get(url, verify=False)
    return response.text

@app.route('/admin')
def admin():
    return "Admin panel - no auth check"

@app.errorhandler(500)
def error_handler(e):
    return str(e)

@app.route('/xxe', methods=['POST'])
def xxe():
    xml_data = request.data
    tree = ET.fromstring(xml_data)
    return ET.tostring(tree)

@app.route('/login')
def login():
    session['user'] = 'guest'

@app.route('/dom_xss')
def dom_xss():
    user_input = request.args.get('input')
    return f"<script>document.write('{user_input}');</script>"

@app.route('/broken_auth')
def broken_auth():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == PASSWORD:
        return "Logged in"

@app.route('/insecure_crypto')
def insecure_crypto():
    key = Fernet.generate_key()
    cipher = Fernet(b'weak_key==')
    return "Encrypted"

@app.route('/buffer_overflow')
def buffer_overflow():
    large_data = 'A' * 1000000
    return large_data

@app.route('/priv_escalation')
def priv_escalation():
    os.setuid(0)

@app.route('/dos')
def dos():
    while True:
        pass

@app.route('/temp_file')
def temp_file():
    tmp = tempfile.mktemp()
    with open(tmp, 'w') as f:
        f.write("sensitive")
    return tmp

@app.route('/ftp')
def ftp():
    ftp = ftplib.FTP('example.com')
    ftp.login('anonymous', '')
    return "Logged in"

@app.route('/insecure_protocol')
def insecure_protocol():
    conn = http.client.HTTPConnection('example.com')
    conn.request("GET", "/")
    return "Response"

@app.route('/cookie')
def cookie():
    resp = make_response("Cookie set")
    resp.set_cookie('session', 'value', secure=False, httponly=False)
    return resp

@app.route('/ip_spoof')
def ip_spoof():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return ip

@app.route('/locale')
def locale():
    loc = request.args.get('locale')
    import locale
    locale.setlocale(locale.LC_ALL, loc)
    return "Set"

@app.route('/sensitive')
def sensitive():
    return "Sensitive data - no check"

@app.route('/deprecated')
def deprecated():
    import imp
    return "Used deprecated"

@app.route('/redos')
def redos():
    pattern = re.compile(r'^(\w+)*$')
    input_str = request.args.get('input')
    re.match(pattern, input_str)
    return "Matched"

@app.route('/admin_interface')
def admin_interface():
    return "Exposed admin"

@app.route('/logic_flaw')
def logic_flaw():
    price = request.args.get('price')
    discount = request.args.get('discount')
    total = int(price) - int(discount)

@app.route('/weak_random')
def weak_random():
    token = random.randint(1, 100)
    return str(token)

@app.route('/jwt_none')
def jwt_none():
    token = request.args.get('token')
    jwt.decode(token, verify=False, algorithms=['none'])
    return "Decoded"

@app.route('/redirect')
def redirect():
    url = request.args.get('url')
    return redirect(url)

@app.route('/coupon')
def coupon():
    code = request.args.get('code')
    if code == "DISCOUNT10":
        return "10% off"

@app.route('/unsafe_html')
def unsafe_html():
    html_content = request.args.get('html')
    return html_content

@app.route('/mass_assignment', methods=['POST'])
def mass_assignment():
    data = request.json
    user = {}
    user.update(data)
    return "Updated"

@app.route('/race')
def race():
    global counter
    counter = 0
    threads = [threading.Thread(target=increment_counter) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return str(counter)

def increment_counter():
    global counter
    temp = counter
    time.sleep(0.1)
    counter = temp + 1

@app.route('/buffer')
def buffer():
    def recursive(n):
        if n > 0:
            recursive(n-1)
    recursive(10000)

@app.route('/yaml_deser')
def yaml_deser():
    data = request.args.get('data')
    obj = yaml.load(data, Loader=yaml.UnsafeLoader)
    return str(obj)

global_state = {}

@app.route('/global_state')
def global_state():
    key = request.args.get('key')
    global_state[key] = request.args.get('value')
    return "Set"

@app.route('/type_error')
def type_error():
    return "1" + 1

@app.route('/accessibility')
def accessibility():
    return '<img src="image.jpg">'

@app.route('/performance')
def performance():
    result = []
    for i in range(1000000):
        result.append(i)
    return "Done"

if __name__ == '__main__':
    app.run(debug=True)
jdk
ash
