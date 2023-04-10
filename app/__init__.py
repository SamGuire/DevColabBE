from flask import Flask
from main.controller.user.user_controller import user_controller

app = Flask(__name__)
app.register_blueprint(user_controller)
@app.route('/')
def hello():
    return "Hello word"
