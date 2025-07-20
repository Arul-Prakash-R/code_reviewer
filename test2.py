from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    ip = request.args.get('ip')  # ?ip=127.0.0.1;ls
    return os.popen(f"ping -c 1 {ip}").read()

app.run(debug=True)
sd
bhsdds
df
