from flask import render_template
from application import app
from application.series.models import Series

@app.route("/")
def index():
    return render_template("index.html", no_episodes=Series.find_series_with_no_episodes())