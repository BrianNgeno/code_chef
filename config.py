import os

class Config():
    '''
    parent class config
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bknngeno:123@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/images'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bknngeno:123@localhost/codechef'
    
    @staticmethod
    def init_app(app):
            pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    pass

config_options = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}