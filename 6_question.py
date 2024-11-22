def validar_cpf(cpf):
    # Remove caracteres não numéricos manualmente
    cpf_numeros = ""
    for caractere in cpf:
        if caractere.isdigit():
            cpf_numeros += caractere

    # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
    if len(cpf_numeros) != 11:
        return False, "O CPF deve ter exatamente 11 dígitos."
    if cpf_numeros == cpf_numeros[0] * 11:
        return False, "O CPF não pode ter todos os números iguais."

    # Função para calcular o dígito verificador
    def calcular_digito(cpf_parcial, peso_inicial):
        soma = 0
        for i, digito in enumerate(cpf_parcial):
            soma += int(digito) * (peso_inicial - i)
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    # Calcula o primeiro dígito verificador
    primeiro_digito = calcular_digito(cpf_numeros[:9], 10)

    # Calcula o segundo dígito verificador
    segundo_digito = calcular_digito(cpf_numeros[:10], 11)

    # Verifica se os dígitos calculados coincidem com os fornecidos
    if cpf_numeros[9] != primeiro_digito:
        return False, f"Primeiro dígito verificador inválido (esperado: {primeiro_digito})."
    if cpf_numeros[10] != segundo_digito:
        return False, f"Segundo dígito verificador inválido (esperado: {segundo_digito})."

    return True, "CPF válido!"


# Entrada do usuário
cpf_informado = input("Digite o CPF (apenas números): ")

# Validação do CPF
valido, mensagem = validar_cpf(cpf_informado)

if valido:
    print(mensagem)
else:
    print(f"CPF inválido! {mensagem}\nNúmero informado: {cpf_informado}")
