def Inicio():
    print(f'El siguiente programa usa diferentes metodos')
    print(f'para calculara la raiz cuadrada de un numero.')
    
    objetivo = int(input('Escoge un entero: '))
    
    temporal = 0
    while temporal < 1:    
        print(f'1. Enumeracion Exhaustiva')
        print(f'2. Aproximación de Soluciones')
        print(f'3. Busqueda Binaria')
        print(f'4. Salir')
        metodo = int(input('Escoge el metodo: '))

        if metodo == 1:
            if enumeracion(objetivo) == 'NN':
                print(f'{objetivo} no tiene una raiz cuadrada exacta usando el metodo de Enumeración Exhaustiva')
            else:
                print(f'La raiz cuadrada de {objetivo} es {enumeracion(objetivo)} usando el metodo de Enumeración Exhaustiva')

        elif metodo == 2:
            if aproximacion(objetivo) == 'NN':
                print(f'No se encontro la raiz cuadrada de {objetivo} usando el metodo de Aproximacion de Soluciones')
            else:
                print(f'La raiz cuadrada de {objetivo} es {aproximacion(objetivo)} usando el metodo de Aproximación de Soluciones')

        elif metodo == 3:
             print(f'La raiz cuadrada de {objetivo} es {busq_binaria(objetivo)} usando el metodo de Busqueda Binaria')

        elif metodo == 4:
            temporal = 1

        else:
            print(f'La opcion escogida no es valida')


def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta +=1

    if respuesta**2 == objetivo:
        return respuesta
    else:
        return 'NN'

def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo)> epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2-objetivo)>= epsilon:
        return 'NN'
    else:
        return respuesta

def busq_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return respuesta

if __name__ == '__main__':
    Inicio()