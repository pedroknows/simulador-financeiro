from decimal import Decimal
from simulador import calcular_parcela_price, gerar_tabela_price

def test_parcela_price_exemplo_simples():
    resultado = calcular_parcela_price(Decimal('1000'), Decimal('0.01'),3)
    assert resultado == Decimal('340.02')

def test_gerar_tabela_price():
    resultado = gerar_tabela_price(Decimal('1000'), Decimal('0.01'),3)
    assert len(resultado) == 3
    mes_dois = resultado[1]
    juros_mes_dois = mes_dois["juros"]
    assert juros_mes_dois == Decimal("6.70")

    mes_tres = resultado[2]
    parcela_mes_tres = mes_tres["parcela"]
    assert parcela_mes_tres == Decimal("340.03")

    saldo_mes_tres = mes_tres["saldo_final"]
    assert saldo_mes_tres == Decimal("0")

    resultado_longo = gerar_tabela_price(Decimal('52191'), Decimal('0.0107'),346)

    saldo_ultimo_mes = resultado_longo[-1]["saldo_final"]
    assert saldo_ultimo_mes == Decimal("0")

    var = 0
    for item in resultado_longo:
        
        assert item["juros"] + item["amortizacao"] == item["parcela"]
        assert item["saldo_inicial"] - item["amortizacao"] == item["saldo_final"]
        var += 1
    