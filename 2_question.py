cpf = input("Digite o CPF (somente números): ")

cpf_limpo = ""
for caractere in cpf:
    if caractere.isdigit():
        cpf_limpo += caractere

print(f"O CPF informado tem {len(cpf_limpo)} dígitos.")
