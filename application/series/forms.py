from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class SeriesForm(FlaskForm):
    name = StringField("Series name", [validators.Length(min=2)])
    episodes_total = IntegerField("Episodes total")

    class Meta:
        csrf = False