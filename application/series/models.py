from application import db
from application.models import Base

from sqlalchemy.sql import text

class Series(Base):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    episodes_total = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.episodes_total = 0;

    @staticmethod
    def find_series_with_no_episodes():
        stmt = text("SELECT name FROM Series WHERE episodes_total = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})
        
        return response
