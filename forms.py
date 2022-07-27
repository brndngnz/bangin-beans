from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL


# Add Cafe Form
class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[URL(), DataRequired()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=["❌", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
                         validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=["❌", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                       validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=["❌", "⚡️", "⚡️⚡️", "⚡️⚡️⚡️", "⚡️⚡️⚡️⚡️", "⚡️⚡️⚡️⚡️⚡️"],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# Registration Form
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Login Form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")