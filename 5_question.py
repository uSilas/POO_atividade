# Entrada: número de termos da série
n_termos = int(input("Digite o número de termos da série de Leibniz: "))

# Fórmula de Leibniz
pi_quartos = 0
for k in range(n_termos):
    termo = (-1)**k / (2*k + 1)
    pi_quartos += termo

pi = pi_quartos * 4
print(f"O valor aproximado de Pi com {n_termos} termos é: {pi:.10f}")
