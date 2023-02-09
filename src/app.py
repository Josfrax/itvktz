from dotenv import dotenv_values
from flask import Flask
from db import db

# Get enviroment variables
env:list = dotenv_values('./.env')

DRIVER_DB:str = env['DRIVER_DB']
HOST_DB:str = env['HOST_DB']
HOST_PORT:int = env['HOST_PORT']
NAME_DB:str = env['NAME_DB']
USER_DB:str = env['USER_DB']
PASS_DB:str = env['PASS_DB']

URI:str = f"{DRIVER_DB}://{USER_DB}:{PASS_DB}@{HOST_DB}:{HOST_PORT}/{NAME_DB}"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=8000, debug=True)