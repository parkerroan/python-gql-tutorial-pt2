from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# db = SQLAlchemy(engine_options={'pool_size':20,'pool_recycle':3600, 'pool_pre_ping':True})
