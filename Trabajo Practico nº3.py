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


#-----------------------------------------------------------------------------------------
# Ejercicio 4
#-----------------------------------------------------------------------------------------


"""

Implemente un algoritmo en Python para calcular el perímetro de un
rectángulo, conociendo su base y altura. Los datos se deben almacenar en
variables, y el resultado se debe mostrar en pantalla.

"""

def perimetroRectangulo(base, altura):
    return (base + altura) * 2

#-----------------------------------------------------------------------------------------
# Ejercicio 5
#-----------------------------------------------------------------------------------------

"""

Implemente un algoritmo en Python para calcular el área de un rectángulo,
conociendo su base y altura. Los datos se deben almacenar en variables, y el
resultado se debe mostrar en pantalla.

"""

def areaRectangulo(base, altura):
    return base * altura


#-----------------------------------------------------------------------------------------
# Ejercicio 6
#-----------------------------------------------------------------------------------------

"""

Implemente un algoritmo que intercambie los valores entre dos variables a y
b cualesquiera. Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la
variable a debería ser igual 5, y la variable b debería ser igual a 10.

"""

def cambiaValores(a,b):
    aux=a
    a=b
    b=aux
    return a,b

#-----------------------------------------------------------------------------------------
# Ejercicio 7
#-----------------------------------------------------------------------------------------

"""

En Python es posible resolver el problema del intercambio de valores sin
hacer uso de variables adicionales, mediante la sintaxis de asignación
múltiple. Investigue de qué se trata dicha funcionalidad, y utilízela para
resolver el ejercicio anterior sin utilizar variables auxiliares/adicionales.

"""
def cambiaValoresMultiple(a,b):
    [a,b]=[b,a]
    return a,b

#-----------------------------------------------------------------------------------------
# Ejercicio 8
#-----------------------------------------------------------------------------------------


"""

Escriba un algoritmo que, conociendo las notas de los dos parciales de un
alumno de la asignatura Introducción a la Programación, muestre en
pantalla su promedio.

"""

def promedioNotas(nota1,nota2):
    return (nota1+nota2)/2

#-----------------------------------------------------------------------------------------
# Ejercicio 9
#-----------------------------------------------------------------------------------------


"""

Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
ahorrada en su cuenta (almacenando ese monto en una variable), muestre
en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
$14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
formato:
Usted tiene $XXX pesos argentinos, los cuales se convierten en:
- U$XXX dólares.
- R$XXX reales.
- €XXX euros.

"""

def convertirAhorros(ahorros):
    return "Usted tiene ${} pesos argentinos, los cuales se convierten en: \n - U${} dólares. \n - R${} reales. \n - €{} euros.".format(ahorros,round(ahorros/80.5,2),round(ahorros/14.1,2),round(ahorros/69.5,2))


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

def testPerimetroRectangulo():
    print('Testeando perimetroRectangulo()... ', end='')
    assert perimetroRectangulo(10,2) == 24
    assert perimetroRectangulo(2,5) == 14
    print('Pasó!')

def testAreaRectangulo():
    print('Testeando areaRectangulo()... ', end='')
    assert areaRectangulo(10,2) == 20
    assert areaRectangulo(2,5) == 10
    print('Pasó!')

def testCambiaValores():
    print('Testeando cambiaValores()... ', end='')
    assert cambiaValores(10,2) == (2,10)
    assert cambiaValores(2,5) == (5,2)
    print('Pasó!')

def testCambiaValoresMultiple():
    print('Testeando cambiaValoresMultiple()... ', end='')
    assert cambiaValoresMultiple(10,2) == (2,10)
    assert cambiaValoresMultiple(2,5) == (5,2)
    print('Pasó!')

def testPromedioNotas():
    print('Testeando promedioNotas()... ', end='')
    assert promedioNotas(10,10) == 10
    assert promedioNotas(7,5) == 6
    print('Pasó!')

def testConvertirAhorros():
    print('Testeando convertirAhorros()... ', end='')
    assert convertirAhorros(100) == "Usted tiene $100 pesos argentinos, los cuales se convierten en: \n - U$1.24 dólares. \n - R$7.09 reales. \n - €1.44 euros."
    print('Pasó!')

#################################################
# testearTodo y main
#################################################

def testearTodo():
    # comentá los tests que no querés correr!
    testValorAbsoluto()
    testCantidadLetras()
    testPotencia()
    testPerimetroRectangulo()
    testAreaRectangulo()
    testCambiaValores()
    testCambiaValoresMultiple()
    testPromedioNotas()
    testConvertirAhorros()

def main():
    testearTodo()

if __name__ == '__main__':
    main()
