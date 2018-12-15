from application import db
from application.models import Base
from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import text

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

        
    @staticmethod
    def find_users_watched_series():
        stmt = text("SELECT account.username AS username, COUNT(user_series.series_id) AS watching, SUM(user_series.episodes_watched) AS eps_watched_total "
                    "FROM account INNER JOIN user_series ON user_series.account_id = account.id "
                    "WHERE user_series.status = 'Watching' "
                    "GROUP BY username "
                    "ORDER BY watching DESC LIMIT 5")

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"username":row[0], "watching":row[1], "eps_watched_total":row[2]})

        return response