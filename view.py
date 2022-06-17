from app import app
from app import db
from flask import render_template
from flask import request
from logics import entropy
from logics import put_in_box
from forms import UserNumber
from models import Developments


def write_to_db(blue, green, red, color, number, box):
    try:
        development = Developments(blue=blue, green=green, red=red, color=color, number=number,
                                   box=str(box))
        db.session.add(development)
        db.session.commit()
        print('yes')
    except:
        print('no')


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        is_digit = request.form['number'].isdigit()
        if is_digit:
            number = int(request.form['number'])
            if number < 1 or number > 100:
                output = 'Введите номер предмета от 1 до 100'
            else:
                entropy_dict = entropy()
                box = put_in_box(entropy_dict)
                color = box[number]
                output = f'Цвет предмета: {color}'

                blue = box.count('blue')
                green = box.count('green')
                red = box.count('red')
                box = f'Предметы: blue: {blue}, green: {green}, red: {red}'

                write_to_db(blue, green, red, color, number, box)

        else:
            output = 'Введите номер предмета от 1 до 100'
    else:
        output = 'Введите номер предмета от 1 до 100'

    form = UserNumber()
    if not 'box' in locals():
        box = ''
    return render_template('index.html', form=form, output=output, box=box)
