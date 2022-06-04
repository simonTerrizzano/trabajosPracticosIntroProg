"""

Trabajo Practico nº 3

"""
#-----------------------------------------------------------------------------------------
# Ejercicio 1
#-----------------------------------------------------------------------------------------
"""

Cree un script que almacene un número entero en una variable, y luego
muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N
es |N|”. Finalmente, verifique que su programa funciona correctamente,
ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego
con el valor -10 (la salida debería ser 10 nuevamente).

"""

def valorAbsoluto(n):

    return "El valor absoluto de {} es |{}|".format(n, abs(n))

#-----------------------------------------------------------------------------------------
# Ejercicio 2
#-----------------------------------------------------------------------------------------

"""

Cree un script que almacene su nombre de pila en una variable, y luego
muestre en pantalla la cantidad de letras de ese nombre, con el mensaje “El
nombre [NOMBRE] tiene [N] letras.”.

"""
def cantidadLetras(nombre):
    return "El nombre {} tiene {} letras.".format(nombre,len(nombre))

#-----------------------------------------------------------------------------------------
# Ejercicio 3
#-----------------------------------------------------------------------------------------

"""

Cree un script que almacene, en dos variables, una base y un exponente, y
luego muestre en pantalla el resultado de elevar el número base a la
potencia exponente.

"""

def potencia(base, exponente):
    return base ** exponente

#################################################
# Funciones de Test
#################################################

def testValorAbsoluto():
    print('Testeando valorAbsoluto()... ', end='')
    assert valorAbsoluto(10) == "El valor absoluto de 10 es |10|"
    assert valorAbsoluto(-10) == "El valor absoluto de -10 es |10|"
    print('Pasó!')

def testCantidadLetras():
    print('Testeando cantidadLetras()... ', end='')
    assert cantidadLetras("Simon") == "El nombre Simon tiene 5 letras."
    assert cantidadLetras("Francesca") == "El nombre Francesca tiene 9 letras."
    print('Pasó!')

def testPotencia():
    print('Testeando potencia()... ', end='')
    assert potencia(10,2) == 100
    assert potencia(2,5) == 32
    print('Pasó!')

#################################################
# testearTodo y main
#################################################

def testearTodo():
    pass
    # comentá los tests que no querés correr!
    # testValorAbsoluto()
    # testCantidadLetras()
    testPotencia()

def main():
    testearTodo()

if __name__ == '__main__':
    main()
