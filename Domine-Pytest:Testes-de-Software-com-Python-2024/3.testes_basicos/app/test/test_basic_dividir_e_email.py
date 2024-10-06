from main import *


def test_email_valido():
    assert valida_email("exemplo@exemplo.com") is True
    assert valida_email("exemplo.com") is False
    
def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,0) is None