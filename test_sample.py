from app.calculate import hipotenusa

def test_1():
    assert hipotenusa(3,4) == 5

def test_2():
    assert hipotenusa(5, 12) == 13

def test_3():
    assert hipotenusa(8, 15) == 17

def test_4():
    assert hipotenusa (8, 15) != 15

