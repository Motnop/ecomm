import os

class Config:
    DEBUG = True
    SECRET_KEY = "UYHA00212uehd89aifbu27i8eyd90uY*WGUF1WEBH23qSAssfJ"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False