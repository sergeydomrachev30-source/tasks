import pytest
from calculate_tax import calculate_tax

def test_calculate_tax():
    assert calculate_tax(100, 10) == 110
    assert calculate_tax(50, 5) == 52.5
    with pytest.raises(ValueError, match="Неверная цена"):
        calculate_tax(-10, 10)
    with pytest.raises(ValueError, match="Неверный налоговый процент"):
        calculate_tax(100, 105)
        calculate_tax(100, -5)
