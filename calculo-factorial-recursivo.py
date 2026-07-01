
def factorial (n):
    if n == 0:
        print('Caso base: 0! = 1')
        return 1
    else:
        resultado = n * factorial(n-1)
        print(f'{n}! = {n} * {n-1}! = {resultado}')
        return resultado
print(f'Resultado= {factorial(5)}')