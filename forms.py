from flask_wtf import Form
from wtforms import StringField, PasswordField, FieldList, FormField
from wtforms.validators import InputRequired, Length, AnyOf

class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)],
    render_kw={"placeholder": "Enter Username"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=15)],
    render_kw={"placeholder": "Enter Password"})

class RegisterForm(Form):
    fullname = StringField('Fullname', validators=[InputRequired(), Length(min=4, max=70)],
    render_kw={"placeholder": "Enter Fullname"})
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)],
    render_kw={"placeholder": "Enter Username"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=15)],
    render_kw={"placeholder": "Enter Password"})

class CustomerForm(Form):
    fullName = StringField('Full name', validators=[InputRequired(), Length(min=4, max=15)],
    render_kw={"placeholder": "Enter full name"})
    mobilePhone = StringField('Mobile phone', render_kw={"placeholder": "Enter mobile phone"})
