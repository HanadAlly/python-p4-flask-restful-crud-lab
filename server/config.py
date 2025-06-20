import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db_uri():
    return os.environ.get('DATABASE_URL', 'sqlite:///plants.db')

