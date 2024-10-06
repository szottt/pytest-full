from main import is_positive

def test_eh_positivo():
    assert is_positive(5) is True
    assert is_positive(-5) is False
    