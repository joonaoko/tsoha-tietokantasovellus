from flask_login import login_required, current_user

from application import db
from application.models import Base

from sqlalchemy.sql import text

class UserSeries(Base):
    episodes_watched = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)

    def __init__(self):
        self.episodes_watched = 0
        self.status = "Watching";

    @staticmethod
    @login_required
    def find_user_series(user_id=0):
        stmt = text("SELECT series.name, user_series.episodes_watched, user_series.status, user_series.id " 
                        "FROM user_series LEFT JOIN series ON user_series.series_id = series.id "
                        "WHERE user_series.account_id = :user_id").params(user_id = current_user.id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"series_name":row[0], "episodes_watched":row[1], "status":row[2], "id":row[3]})

        return response