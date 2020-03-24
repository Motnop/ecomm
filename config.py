import os

class Config:
    DEBUG = True
    SECRET_KEY = "UYHA00212uehd89aifbu27i8eyd90uY*WGUF1WEBH23qSAssfJ"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:1234@127.0.0.1:5432/ecomm"
    SQLALCHEMY_TRACK_MODIFICATIONS = False