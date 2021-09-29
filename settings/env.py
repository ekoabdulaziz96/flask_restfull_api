"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

FLASK_APP = env.str("FLASK_APP", default="server.py")
ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
# BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
# DEBUG_TB_ENABLED = DEBUG
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
