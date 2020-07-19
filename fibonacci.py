def fibonacci (n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Escribe un entero: '))
print(f'La serie de Fibonacci para {n} es de {fibonacci(n)}')
