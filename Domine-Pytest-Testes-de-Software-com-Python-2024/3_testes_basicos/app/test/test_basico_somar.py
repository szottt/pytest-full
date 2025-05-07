from main import somar, comprimento

def test_somar_e_comprimento():
    assert somar(3,2) == 5
    assert comprimento([1,2,3,4,5]) == 5