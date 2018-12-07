from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, validators, widgets

class UserSeriesUpdateForm(FlaskForm):
    episodes_watched = IntegerField("Episodes watched",
                                    [validators.NumberRange(min=0, max=99999)],
                                    widget=widgets.Input(input_type="number"))
    status = SelectField("Status", choices=[('Watching', 'Watching'), ('Maybe', 'Maybe')])

    class Meta:
        csrf = False