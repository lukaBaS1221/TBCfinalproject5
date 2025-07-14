from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, PasswordField, DateField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, length, equal_to
from wtforms import TextAreaField


class RegisterForm(FlaskForm):
    profile_img = FileField("choose your profile picture", validators=[FileRequired()])
    username=StringField("enter your username", validators=[DataRequired()])
    password = PasswordField("choose a password", validators=[DataRequired(), length(min=8, max=22)])
    confirm_password = PasswordField("confirm password", validators=[DataRequired(), equal_to("password")])
    birthday = DateField("select your birth date", validators=[DataRequired()])
    gender = RadioField("choose your gender", choices=["male", "female"], validators=[DataRequired()])
    country = SelectField(choices=["choose your home country", "georgia", "USA", "UK", ""], validators=[DataRequired()])

    submit = SubmitField("registrate")  

class LoginForm(FlaskForm):
        username = StringField("enter your username", validators=[DataRequired()])
        password = PasswordField("enter your password", validators=[DataRequired()])
        submit = SubmitField("login")




class BookForm(FlaskForm):
    title = StringField("book name", validators=[DataRequired(), length(min=2, max=100)])
    author = StringField("author", validators=[DataRequired(), length(min=2, max=100)])
    price = StringField("price (₾)", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired(), length(max=1000)])
    cover_image = FileField("book image", validators=[FileRequired(), FileAllowed(["png", "jpeg", "jpg"])])
    submit = SubmitField("add book")
