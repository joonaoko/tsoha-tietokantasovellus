from application import db
from application.models import Base
from sqlalchemy import UniqueConstraint

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), unique=True, nullable=False)
    password = db.Column(db.String(144), nullable=False)

    series = db.relationship("Series", backref='account', lazy=True)

    role = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.role = "USER"
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role