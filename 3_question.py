n = int(input("Informe um número inteiro para a sequência de Fibonacci: "))

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n + 1):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

resultado = fibonacci(n)
print(f"Série de Fibonacci até o {n}º termo: {resultado}")
