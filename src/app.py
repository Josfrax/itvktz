from connexion import App
from dotenv import dotenv_values
from db import db
from ma import ma

# Create the application instance
conn = App("__name__",specification_dir='./src/')

# Read the swagger to configure the endpoints
conn.add_api('swagger.yml')
app = conn.app

# Get enviroment variables
env:list = dotenv_values('./.env')

# Get Values of eviroments
DRIVER_DB:str = env['DRIVER_DB']
HOST_DB:str = env['HOST_DB']
HOST_PORT:int = env['HOST_PORT']
NAME_DB:str = env['NAME_DB']
USER_DB:str = env['USER_DB']
PASS_DB:str = env['PASS_DB']

# Connection with db
URI:str = f"{DRIVER_DB}://{USER_DB}:{PASS_DB}@{HOST_DB}:{HOST_PORT}/{NAME_DB}"
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

# Create Table
@app.before_first_request
def create_tables():
    db.create_all()

# Run App
if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=8000, debug=True)