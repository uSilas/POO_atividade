while True:
    # inputs
    investimento_mensal = float(input("Quanto será investido por mês (em R$)? "))
    taxa_juros = float(input("Qual é a taxa de juros mensal (em %)? ")) / 100
    saldo = 0

    # calculo de cada mes por 12 meses
    for _ in range(12):
        saldo += investimento_mensal
        saldo += saldo * taxa_juros

    print(f"Saldo final em 1 ano: R$ {saldo:.2f}")
    break
