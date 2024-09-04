from flask import Flask
from config import DevelopmentConfig, TestingConfig, Config
import os
from dotenv import load_dotenv
from community_app.routes.questions import questions_bp
from community_app.routes.responses import response_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



migrate = Migrate()
db = SQLAlchemy()
app = Flask(__name__)
load_dotenv()

config_name = os.getenv('FLASK_ENV')


@app.route('/')
def home_page():
    return 'Welcome to homepage'


config_set_up = {
    'production': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}.get(config_name)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)

    return app