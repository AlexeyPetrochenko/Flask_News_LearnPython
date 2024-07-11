from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField(label='Пароль', validators=[DataRequired(message='Пароль не может быть пустым')], render_kw={'class': 'form-control'})
    remember_me = BooleanField(label='Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Войти', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    password = PasswordField(label='Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password2 = PasswordField(
        label='Повторите пароль',
        validators=[DataRequired(), EqualTo(fieldname='password', message='Пароли не совпадают')],
        render_kw={'class': 'form-control'}
    )
    submit = SubmitField('Войти', render_kw={'class': 'btn btn-primary'})

    def validate_username(self, username):
        count_user = User.query.filter_by(username=username.data).count()
        if count_user > 0:
            raise ValidationError('пользователь с таким именем уже существует')

    def validate_email(self, email):
        count_user = User.query.filter_by(email=email.data).count()
        if count_user > 0:
            raise ValidationError('На этот email уже зарегистрирован аккаунт')
