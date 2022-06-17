from wtforms import Form, StringField


class UserNumber(Form):
    number = StringField('Введите номер предмета')
