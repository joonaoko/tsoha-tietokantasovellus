from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators, widgets

class UserSeriesUpdateForm(FlaskForm):
    episodes_watched = IntegerField("Episodes watched", 
                                    [validators.NumberRange(min=0, max=99999)],
                                    widget=widgets.Input(input_type="number"))
    status = StringField("Status", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False