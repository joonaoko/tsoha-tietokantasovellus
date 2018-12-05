from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.userseries.models import UserSeries
from application.series.models import Series
from application.userseries.forms import UserSeriesUpdateForm

from sqlalchemy.sql import text

@app.route("/userseries", methods=["GET"])
@login_required
def userseries_index():
    return render_template("userseries/list.html", userseries = UserSeries.find_user_series())

@app.route("/userseries/update/<userseries_id>/")
@login_required
def userseries_update_form(userseries_id):
  us = UserSeries.query.get(userseries_id)
  s = Series.query.get(us.series_id)
  return render_template("userseries/update.html", userseries = us, series = s, form = UserSeriesUpdateForm())

@app.route("/userseries/plus1/<userseries_id>/", methods=["POST"])
@login_required
def userseries_increase_episodes_watched_by_one(userseries_id):
    us = UserSeries.query.get(userseries_id)
    us.episodes_watched += 1
    db.session().commit()

    return redirect(url_for("userseries_index"))

@app.route("/userseries/update/<userseries_id>/", methods=["POST"])
@login_required
def userseries_update(userseries_id):
  form = UserSeriesUpdateForm(request.form)

  if not form.validate():
    return render_template("userseries/update.html", form = form)

  us = UserSeries.query.get(userseries_id)
  us.episodes_watched = form.episodes_watched.data
  us.status = form.status.data
  db.session().commit()

  return redirect(url_for("userseries_index"))

@app.route("/userseries/delete/<userseries_id>/", methods=["POST"])
@login_required
def userseries_delete(userseries_id):
    stmt = text("DELETE FROM user_series WHERE id = :id").params(id=userseries_id)
    db.engine.execute(stmt)
    db.session().commit()

    return redirect(url_for("userseries_index")) 