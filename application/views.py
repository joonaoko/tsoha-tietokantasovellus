from flask import render_template
from application import app
from application.series.models import Series
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", most_popular=Series.find_most_popular_series(), recently_watched=Series.find_recently_watched_series(), users_series=User.find_users_watched_series())