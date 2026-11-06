from decimal import Decimal, ROUND_HALF_UP

def calcular_parcela_price(valor, taxa_mensal, meses):
    fator = (1 + taxa_mensal)**(-meses)
    parcela = (valor * taxa_mensal) / (1 - fator)
    parcela_final = parcela.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return parcela_final

def gerar_tabela_price(valor, taxa_mensal, meses):
    lista_valores = []
    valor_parcela = calcular_parcela_price(valor, taxa_mensal, meses)
    for i in range(1, meses + 1):
        juros_total = (valor * taxa_mensal).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        amortizacao = (valor_parcela - juros_total)
        saldo_remanescente = valor - amortizacao
        if i == meses:
            valor_parcela += saldo_remanescente
            amortizacao += saldo_remanescente
            saldo_remanescente = Decimal("0")
                

        lista_valores.append({"mes":i,
                               "saldo_inicial":valor,
                                 "juros":juros_total,
                                   "amortizacao":amortizacao,
                                     "parcela":valor_parcela,
                                       "saldo_final":saldo_remanescente})
        valor -= amortizacao
    return lista_valores