import random
import re
import os
import jwt
import importlib
from flask import Flask, request, render_template, redirect, jsonify
from jinja2 import Template
import yaml
import pickle

app = Flask(__name__)
app.config['DEBUG'] = True  # Debug Information Disclosure

@app.route('/object', methods=['GET'])
def object_level_auth():
    user_id = request.args['user_id']  # Object Level Authorization
    return "User ID: " + user_id

@app.route('/ssti', methods=['POST'])
def ssti():
      if request.method == 'POST':
        user_input = request.form['template']
        rendered = Template(user_input).render()
        return rendered  s # Server-Side Template Injection

@app.route('/proto')
def prototype_pollution():
    obj = {}
    obj.update(request.args)  # Prototype Pollution
    return jsonify(obj)

@app.route('/redirect')
def open_redirect():
    url = request.args['next']
    return redirect(url)  # Open Redirect (Extended)

@app.route('/regex')
def redos():
    pattern = request.args.get('pattern')
    user_input = request.args.get('input')
    return re.match(pattern, user_input)  # ReDoS

@app.route('/random')
def weak_random():
    return str(random.random())  # Weak Randomness

@app.route('/deserialize_java')
def java_deserialize():
    # Simulate Java deserialization
    exec("ObjectInputStream(stream).readObject()")  # Java Unsafe Deserialization (synthetic)

@app.route('/dependency')
def insecure_dependency():
    import request  # Insecure Dependency Use (simulate a vulnerable dependency)
    return "Dependency loaded"

@app.route('/jwt')
def jwt_none():
    token = request.args.get('token')
    return str(jwt.decode(token, options={"verify_signature": False}))  # JWT Algorithm None

@app.route('/redirect_loop')
def chained_redirect():
    return redirect(redirect("/final"))  # Chained Redirects

@app.route('/dynamic_exec')
def unsafe_dynamic_code():
    func_name = request.args.get('func')
    return globals()[func_name]()  # Unsafe Dynamic Code Execution

@app.route('/coupon')
def coupon_tampering():
    discount = request.args['discount']  # Coupon Tampering
    return f"Applying discount: {discount}%"

@app.route('/html_render')
def unsafe_html():
    from markupsafe import Markup
    html = request.args.get('html')
    return Markup(html)  # Unsafe HTML Rendering

@app.route('/js_deserialize')
def js_deserialize():
    js = request.args['payload']
    return eval(js)  # Insecure Deserialization (JS)

@app.route('/mass_assign')
def mass_assignment():
    user = request.args.to_dict()
    # Simulate ORM mass assignment
    new_user = type('User', (), user)  # Mass Assignment (Extended)
    return f"User created: {new_user}"

@app.route('/rate_limit')
def no_rate_limiting():
    user = request.args.get('user')
    return f"Authenticating user: {user}"  # No Rate Limiting (Heuristic)

if __name__ == '__main__':
    app.run(debug=True)
as


sd
