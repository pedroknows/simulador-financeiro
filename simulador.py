def calcular_parcela_price(valor, taxa_mensal, meses):
    fator = (1 + taxa_mensal)**(-meses)
    parcela = round((valor * taxa_mensal) / (1 - fator), 2)
    print(parcela)
    return parcela