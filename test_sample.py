from app.calculate import hipotenusa

def test_vista():
    assert hipotenusa(3,4) == 5

def test_otro_valor():
    assert hipotenusa(5, 12) == 13

