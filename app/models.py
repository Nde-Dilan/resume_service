from . import db

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)
    filepath = db.Column(db.String(256), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=db.func.now())
