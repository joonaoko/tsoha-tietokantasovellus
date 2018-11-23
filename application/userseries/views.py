from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.userseries.models import UserSeries
from application.userseries.forms import UserSeriesForm

from sqlalchemy.sql import text

@app.route("/userseries", methods=["GET"])
@login_required
def userseries_index():
    return render_template("userseries/list.html", userseries = UserSeries.find_user_series())

@app.route("/userseries/plus1/<userseries_id>/", methods=["POST"])
@login_required
def userseries_increase_episodes_watched_by_one(userseries_id):
    us = UserSeries.query.get(userseries_id)
    us.episodes_watched += 1
    db.session().commit()

    return redirect(url_for("userseries_index"))

@app.route("/userseries/delete/<userseries_id>/", methods=["POST"])
@login_required
def userseries_delete(userseries_id):
    stmt = text("DELETE FROM user_series WHERE id = :id").params(id=userseries_id)
    db.engine.execute(stmt)
    db.session().commit()

    return redirect(url_for("userseries_index")) 