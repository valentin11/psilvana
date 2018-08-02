from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
Bootstrap(app)
login_manager.init_app(app)

from views import *

if __name__ == '__main__':
	app.run(debug=DEBUG)
