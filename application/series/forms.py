from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SeriesForm(FlaskForm):
    name = StringField("Series name", [validators.Length(min=2)])
    episodes_total = IntegerField("Episodes total", [validators.Length(min=1)])

    class Meta:
        csrf = False