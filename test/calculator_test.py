import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)


import calculator


def test_calc_addition():
    output = calculator.add(1, 2)
    assert output == 3


def test_calc_substraction():
    output = calculator.substract(3, 1)
    assert output == 2


def test_calc_multiply():
    output = calculator.multiply(2, 3)
    assert output == 6
