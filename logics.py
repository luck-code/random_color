from random import randint
from random import shuffle


def put_in_box(entropy_dict):
    box = []
    blue = entropy_dict['blue']
    green = entropy_dict['green']
    red = entropy_dict['red']

    blue_box = ['blue' for time in range(blue)]
    green_box = ['green' for time in range(green)]
    red_box = ['red' for time in range(red)]
    box = [None] + blue_box + green_box + red_box
    shuffle(box)
    return box


def entropy():
    # blue = 70  # (51-97)
    # red = 10  # (1-24)
    # green = 20  # (2-25)
    ent = {}
    blue = randint(51, 97)
    rest = 100 - blue
    red = randint(1, rest)
    green = 100 - (blue + red)

    if green == 0:
        blue -= 1
        green += 1

    if green < red:
        green, red = red, green

    if green == red:
        green += 1
        red -= 1

    ent['blue'] = blue
    ent['green'] = green
    ent['red'] = red
    ent['sum'] = blue + red + green

    return ent
