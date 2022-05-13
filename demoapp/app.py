from crypt import methods
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def home():
    return 'render_templateeee(mostrar.html)'

@app.route('/saludar')
def saludar():
    return 'saludos'

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')