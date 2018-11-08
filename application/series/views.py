from application import app, db
from flask import redirect, render_template, request, url_for
from application.series.models import Series

@app.route("/series", methods=["GET"])
def series_index():
    return render_template("series/list.html", series = Series.query.all())

@app.route("/series/new/")
def series_form():
    return render_template("series/new.html")

@app.route("/series/<series_id>/", methods=["POST"])
def series_set_episodes_total(series_id):
    s = Series.query.get(series_id)
    s.episodes_total += 1
    db.session().commit()

    return redirect(url_for("series_index"))

@app.route("/series/", methods=["POST"])
def series_create():
    s = Series(request.form.get("name"))

    db.session().add(s)
    db.session().commit()
  
    return redirect(url_for("series_index"))
