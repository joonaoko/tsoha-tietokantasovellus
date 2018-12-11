from application import db
from application.models import Base

from sqlalchemy.sql import text

import os

class Series(Base):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    episodes_total = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.episodes_total = 0;

    @staticmethod
    def find_series():
        stmt = text("SELECT id, name, episodes_total "
                    "FROM series "
                    "ORDER BY series.name ASC")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "episodes_total":row[2]})

        return response

    @staticmethod
    def find_series_with_no_episodes():
        stmt = text("SELECT name FROM Series WHERE episodes_total = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})
        
        return response

    @staticmethod
    def find_most_popular_series():
        stmt = text("SELECT series.name AS name, COUNT(user_series.series_id) AS amount "
                    "FROM user_series INNER JOIN series ON user_series.series_id = series.id "
                    "GROUP BY series.name "
                    "ORDER BY amount DESC LIMIT 5")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "amount":row[1]})

        return response

    @staticmethod
    def find_recently_watched_series():
        if os.environ.get("HEROKU"):
            stmt = text("SELECT DISTINCT ON (series.id) series.name AS name FROM ("
                            "SELECT series.id, series.name, user_series.date_modified "
                            "FROM user_series INNER JOIN series ON user_series.series_id = series.id "
                            "WHERE user_series.date_modified >= now() - interval '24 hour' "
                            "ORDER BY user_series.date_modified DESC LIMIT 10) q")
        else: 
            stmt = text("SELECT DISTINCT series.id, series.name AS name "
                        "FROM user_series INNER JOIN series ON user_series.series_id = series.id "
                        "WHERE user_series.date_modified >= datetime('now','-1 day') "
                        "ORDER BY user_series.date_modified DESC LIMIT 10")

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[1]})

        return response
