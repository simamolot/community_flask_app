import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')



class DevelopmentConfig(Config):
    Debug = True


class TestingConfig(Config):
    Debug = True
    Testing = True