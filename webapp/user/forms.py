from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField(label='Пароль', validators=[DataRequired(message='Пароль не может быть пустым')], render_kw={'class': 'form-control'})
    remember_me = BooleanField(label='Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Войти', render_kw={'class': 'btn btn-primary'})
