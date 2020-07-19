def Inicio():
    a = int(input('Ingrese un numero (a): '))
    b = int(input('Ingrese otro numero (b): '))
    print(f'La suma es {suma(a,b)}')

def suma(a,b):
    """ Suma dos valores a y b.

    param int a cualquier entero
    param int b cualquier entero
    returns la sumatoria de a y b
    """
    total = a + b
    return total

if __name__ == '__main__':
    Inicio()
