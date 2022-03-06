# -*- coding: utf-8 -*-
"""
@author: gorbizone

Module 0 from PyCamp Bootcamp named TotoLotek
"""


from random import sample


def take_user_numbers():
    """
    Retrieve data from the user

    Returns
    -------
    numbers : set
        Numbers indicated by the user.

    """
    numbers = set()
    i = 1

    while i in range(7):
        number = input(f'Podaj liczbę {i}: ')
        if int(number) in numbers:
            print('Podałes już taką liczbę')
        elif int(number) >= 1 and int(number) <= 49:
            numbers.add(int(number))
            i += 1
        else:
            print('Podałes liczbę spoza zakresu [1-49]')
    return numbers


def drawing_machine():
    """
    Generate random numbers by machine

    Returns
    -------
    set: machine generated numbers

    """
    return set(sample(range(1, 50), 6))


def draw_before_win(numbers, drawing_numbers):
    """
    Drawing until win

    Parameters
    ----------
    numbers : set
        Numbers indicated by the user.
    drawing_numbers : set
        Generated random numbers by drawing_machine function.

    Returns
    -------
    drawing_counter : int
        Number of performed draw.

    """
    drawing_counter = 0
    drawing_numbers = {}

    while numbers != drawing_numbers:
        drawing_numbers = drawing_machine()
        drawing_counter += 1

    return drawing_counter


if __name__ == '__main__':
    COUNTER = draw_before_win(take_user_numbers(), drawing_machine)
    COST = COUNTER * 3
    print(f'Aby wygrać musiałes wziąć udział w {COUNTER} losowaniach.')
    print(f'Poniosłes koszt w wysokosci {COST: .2f} zł')
