from decimal import Decimal
from simulador import calcular_parcela_price

def test_parcela_price_exemplo_simples():
    resultado = calcular_parcela_price(1000, 0.01, 3)
    assert resultado == 340.02