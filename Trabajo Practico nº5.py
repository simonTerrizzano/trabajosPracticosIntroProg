from modulo_cadena import *

"""

Trabajo Practico nº 3

"""
#-----------------------------------------------------------------------------------------
# Ejercicio 1
#-----------------------------------------------------------------------------------------

"""

Cree una función que reciba dos números como parámetro, y muestre en
pantalla la suma aritmética de ambos. Invoque a la función con dos números
leídos desde teclado.

"""

from subprocess import HIGH_PRIORITY_CLASS


def inputSuma():
    n1=int(input("Ingrese el 1er numero: "))
    n2=int(input("Ingrese el 2do numero: "))
    print(f"la suma de {n1} y {n2} es: {(n1+n2)}")

#-----------------------------------------------------------------------------------------
# Ejercicio 2
#-----------------------------------------------------------------------------------------

"""

Modifique el script del ejercicio anterior para que la función retorne el resultado
en vez de mostrarlo. El programa debe seguir mostrando el resultado en
pantalla.

"""

def suma(a,b):
     return a+b

def inputSuma():
    n1=int(input("Ingrese el 1er numero: "))
    n2=int(input("Ingrese el 2do numero: "))
    print(f"la suma de {n1} y {n2} es: {suma(n1,n2)}")


#-----------------------------------------------------------------------------------------
# Ejercicio 3
#-----------------------------------------------------------------------------------------

"""

Cree una función que reciba un string como parámetro, y retorne la cantidad de
letras que posee. Luego, utilice la función para escribir un programa que solicite
ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
ese nombre.

"""

def largoPalabra(p):
    cont=0
    for letra in p:
        if letra == letra:
            cont+= 1
    return cont

def largoNombre():
    nombre=str(input("Ingrese su nombre para saber su largo: "))
    print(f"Su nombre tiene {largoPalabra(nombre)}")


#-----------------------------------------------------------------------------------------
# Ejercicio 4
#-----------------------------------------------------------------------------------------

"""

Cree una función que reciba dos números como parámetro (base y exponente),
y retorne el resultado de elevar base a la potencia exponente.

"""

def potencia(base, exponente):
    return base ** exponente

#-----------------------------------------------------------------------------------------
# Ejercicio 5
#-----------------------------------------------------------------------------------------

"""

Cree una función que reciba un string como parámetro, y retorne el mismo
string, pero con todas las letras convertidas a mayúsculas.

"""

def mayus(p):
    return p.upper()

#-----------------------------------------------------------------------------------------
# Ejercicio 6
#-----------------------------------------------------------------------------------------

"""
Modifique la función del ejercicio anterior para que retorne dos versiones del
string recibido como parámetro: primero la versión en minúsculas, y luego la
versión en mayúsculas.

"""

def mayusYminus(p):
    return p.lower(), p.upper()

#-----------------------------------------------------------------------------------------
# Ejercicio 7
#-----------------------------------------------------------------------------------------

"""

Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
y retorne True si nombre1 tiene más letras que nombre2, o False en caso
contrario.

"""

def comparaLargo(nombre1,nombre2):
    
    if len(nombre1) > len(nombre2):
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------
# Ejercicio 7
#-----------------------------------------------------------------------------------------

"""

Cree un archivo llamado modulo_cadena.py; dentro de él, cree una función
llamada leer_cadena que, sin recibir ningún parámetro, le solicite al usuario leer
un string cualquiera, y luego lo retorne. Luego cree otro archivo llamado
programa_principal.py, que ejecute el programa haciendo uso de la función
creada en el otro archivo.

"""

def llamarModulo():
    print(leerCadena())

llamarModulo()