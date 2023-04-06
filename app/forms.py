from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, FieldList
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=100)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Create")


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=100)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class AstroForm(FlaskForm):
    add = SubmitField(label="Add items")
    select = BooleanField()
    results = FieldList(BooleanField("Name"))
    item = StringField("Astro", validators=[DataRequired()])
