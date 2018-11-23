from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class UserSeriesForm(FlaskForm):
    episodes_watched = IntegerField("Episodes watched")

    class Meta:
        csrf = False