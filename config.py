import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_USE_TLS = 'true'
    MAIL_PORT = '587'
    MAIL_USERNAME = 'ischoolcode@sina.com'
    MAIL_PASSWORD = 'ixiaoma'
    FLASKY_MAIL_SUBJECT_PREFIX = 'Dear'
    FLASKY_MAIL_SENDER = 'i school code <ischoolcode@sina.com>'
    FLASKY_ADMIN = 'chenzikangyoder@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@192.168.220.117:3306/test'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@192.168.220.117:3306/test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@192.168.220.117:3306/test'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
