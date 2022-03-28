import APC

import pytest


@pytest.mark.areaof
def test_area_square():
    a = 7

    Res = APC.area_square(a)
    assert Res == a**2


@pytest.mark.periof
def test_perimeter_rectangle():
    ln = 7
    bd = 2

    Res = APC.perimeter_rectangle(ln, bd)
    assert Res == 2 * (ln + bd)


@pytest.mark.areaof
def test_area_rectangle():
    ln = 2
    bd = 4

    Res = APC.area_rectangle(ln, bd)
    assert Res == ln * bd



