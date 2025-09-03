# insecure_demo.py
# INTENTIONALLY VULNERABLE — for educational use in a closed lab only

from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import requests

app = Flask(__name__)

# ======================
# CORS MISCONFIGURATION
# Reflects origin, allows credentials
# ======================
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

socketio = SocketIO(app, cors_allowed_origins="*")  # ❌ allows any origin


# ======================
# CLICKJACKING
# No X-Frame-Options or CSP headers set
# ======================
@app.route("/sensitive")
def sensitive():
    html = """
    <h1>Account Transfer</h1>
    <form method="POST" action="/transfer">
      <input name="to" value="attacker" />
      <input name="amount" value="1000" />
      <button type="submit">Transfer</button>
    </form>
    """
    resp = make_response(html)
    # ❌ Missing X-Frame-Options / CSP
    return resp


@app.route("/transfer", methods=["POST"])
def transfer():
    return "Transfer initiated (demo)."


# ======================
# INSECURE API USAGE
# User controls target URL, SSRF possible
# ======================
@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    try:
        # ❌ Insecure: allows arbitrary URLs, cleartext HTTP, no allowlist
        r = requests.get(url, timeout=5, verify=False)
        return jsonify({"ok": True, "from": url, "status": r.status_code, "data": r.text[:200]})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


# ======================
# HOMEPAGE: triggers insecure WS + CORS
# ======================
@app.route("/")
def index():
    return send_file("index.html")


# ======================
# INSECURE WEBSOCKET USAGE
# No origin checks, no auth, leaks secrets
# ======================
@socketio.on("connect")
def handle_connect():
    print("Client connected:", request.sid)
    # ❌ Leak secret on connect
    emit("secret", {"token": "demo-leak-123", "userEmail": "user@example.com"})


@socketio.on("msg")
def handle_message(msg):
    # ❌ Echo back without validation
    emit("msg", msg, broadcast=True)


if __name__ == "__main__":
    # ❌ Runs over HTTP (ws://), not HTTPS (wss://)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
s
as
as
