from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Required()])
    password = PasswordField("Password", [validators.Required()])
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Required(), validators.Length(min=2, max=144)])
    username = StringField('Username', [validators.Required(), validators.Length(min=2, max=20)])
    password = PasswordField('Password', [validators.Required(), validators.Length(min=5, max=144)])

    class Meta:
        csrf = False
    
