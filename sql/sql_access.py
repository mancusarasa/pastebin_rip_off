from flask_sqlalchemy import SQLAlchemy
from app import db


class Paste(db.Model):
    # records in this table represent a translation between the hash
    # the user knows (called paste_id here) and the path of the paste in the object store
    paste_id = db.Column(db.String(10), primary_key=True, nullable=False) # this is the hash that the user knows
    paste_path = db.Column(db.String(10), nullable=False) # this path is relative to the object store


def get_paste(paste_id):
    return Paste.query.filter_by(paste_id=paste_id).first()

def get_all_pastes():
    result = Paste.query.all()
    return result

def create_paste(paste_id, paste_path):
    paste = Paste(paste_id=paste_id, paste_path=paste_path)
    db.session.add(paste)
    db.session.commit()

def cache_random_shit():
    create_paste('1', 'apath')
