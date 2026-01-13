import pytest
from tax_calculator import calculate_taxes


# Тест на корректный результат
def test_calculate_taxes_correct():
    assert calculate_taxes([100.0, 200.0], 10.0) == [110.0, 220.0]


# Тест на "Неверная цена"
def test_calculate_taxes_invalid_price():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes([0], 10.0)


# Тест на "Неверный налоговый процент"
def test_calculate_taxes_invalid_tax_rate():
    with pytest.raises(ValueError, match="Неверный налоговый процент"):
        calculate_taxes([100.0], -10.0)


# Фикстура для примеров данных
@pytest.fixture
def example_data():
    return {
        'prices': [100.0, 200.0],
        'tax_rate': 10.0,
        'expected_result': [110.0, 220.0]
    }


# Тесты с использованием фикстуры

def test_calculate_taxes_with_fixture(example_data):
    prices = example_data['prices']
    tax_rate = example_data['tax_rate']
    expected = example_data['expected_result']
    assert calculate_taxes(prices, tax_rate) == expected


# Тест на корректный результат
@pytest.mark.parametrize("prices, tax_rate, expected", [
    ([100.0, 200.0], 10.0, [110.0, 220.0]),
    ([50.0, 150.0], 20.0, [60.0, 180.0]),
])
def test_calculate_taxes_correct(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


# Тест на "Неверная цена"
@pytest.mark.parametrize("prices, tax_rate", [
    ([0], 10.0),
    ([-10.0], 5.0),
])
def test_calculate_taxes_invalid_price(prices, tax_rate):
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes(prices, tax_rate)


def test_calculate_taxes_zero_tax_rate():
    assert calculate_taxes([100.0, 200.0], 0.0) == [100.0, 200.0]


# Тест на нулевую цену
def test_calculate_taxes_zero_price():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes([0.0], 10.0)


@pytest.mark.parametrize("prices, tax_rate", [
    ([0.01], 0.01),
    ([1000000.0], 100.0), ])
def test_calculate_taxes_boundary_values(prices, tax_rate):
    pass
