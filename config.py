import os

base_dir = os.path.abspath(os.path.dirname(__file__))
FLASK_APP = 'app.py'
DEBUG = True

class Config(object):

    # Enter your Open API Key here or setup environment variables
    OPENAI_API_KEY = os.environ["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"]
    FINNHUB_API_KEY = os.environ["cse5lnpr01qs1ihofsegcse5lnpr01qs1ihofsf0"]
    

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'test.db')
