import pytest

from mypkg.my_answers import numbers_and_strings

x, y, z, length, m, n = numbers_and_strings()


def test_power():
    assert(x == 4120900)


def test_string():
    assert(y == "Python")


def test_repeat():
    assert(len(z) == 10 * len("Python"))


def test_len():
    assert(length == 60)


def test_concat():
    assert(m == "Python is Great")


def test_replace():
    assert(n == "Python is good")


