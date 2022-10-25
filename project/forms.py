from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField, StringField
from wtforms.validators import DataRequired, InputRequired, Length



class SignForm(FlaskForm):
    name = StringField('Ваше имя: ', validators=[DataRequired(), Length(min=2)])
    date = DateField('Дата рождения: ', validators=[InputRequired()])
    submit = SubmitField('Посмотреть свой гороскоп')