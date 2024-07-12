from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('dobro.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/start/addition')
def addition():
    return render_template('addition.html')

@app.route('/start/division')
def division():
    return render_template('division.html')

@app.route('/start/multiplication')
def multiplication():
    return render_template('multiplication.html')

@app.route('/start/substraction')
def substraction():
    return render_template('substraction.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/apple')
def login_apple():
    return render_template('apple.html')

@app.route('/login/goog')
def login_google():
    return render_template('goog.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/signup')
def sign_up():
    return render_template('sign_up.html')

app.run(host='0.0.0.0', port=8000, debug=True)