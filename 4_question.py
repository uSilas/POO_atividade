while True:
    # inputs
    investimento_mensal = float(input("Quanto será investido por mês (em R$)? "))
    taxa_juros = float(input("Qual é a taxa de juros mensal (em %)? ")) / 100
    saldo = 0

    # calculo de cada mes por 12 meses
    for _ in range(12):
        saldo += investimento_mensal
        saldo += saldo * taxa_juros

    print(f"Saldo do investimento após 1 ano: R$ {saldo:.2f}")
    
    # Perguntar ao usuário se quer mais um ano
    continuar = input("Deseja processar mais um ano? (S/N): ").strip().upper()
    if continuar != 'S':
        break
