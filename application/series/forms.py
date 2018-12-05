from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, widgets

class SeriesForm(FlaskForm):
    name = StringField("Series name", [validators.Length(min=2, max=144)])
    episodes_total = IntegerField("Episodes total", 
                                   [validators.NumberRange(min=0, max=99999)],
                                   widget=widgets.Input(input_type="number"))

    class Meta:
        csrf = False

class SeriesEpisodesTotalForm(FlaskForm):
    episodes_total = IntegerField("Episodes total",
                                   [validators.NumberRange(min=0, max=99999)],
                                   widget=widgets.Input(input_type="number"))
    
    class Meta:
        csrf = False

class SeriesUpdateForm(FlaskForm):
    name = StringField("Series name", [validators.Length(min=2, max=144)])
    episodes_total = IntegerField("Episodes total", 
                                   [validators.NumberRange(min=0, max=99999)],
                                   widget=widgets.Input(input_type="number"))

    class Meta:
        csrf = False