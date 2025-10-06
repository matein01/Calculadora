import math

def suma(numUno, numDos):
    return numUno + numDos

def resta(numUno, numDos):
    return numUno - numDos

def multiplicacion(numUno, numDos):
    return numUno * numDos

def division(numUno, numDos):
    if numDos == 0:
        return "Error: Division by zero"
    return numUno / numDos

def potencia(base, exponente):
    return math.pow(base, exponente)

def raiz_cuadrada(num):
    if num < 0:
        return "Error: Negative input for square root"
    return math.sqrt(num)

def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    return math.tan(math.radians(angulo))

def logaritmo(num, base):
    if num <= 0:
        return "Error: Non-positive input for logarithm"
    if base <= 1:
        return "Error: Logarithm base must be greater than 1"
    return math.log(num, base)

opcion = 11

while True:
    print("Seleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz Cuadrada")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("11. Salir")
    opcion = input("Ingrese su opcion (1-11): ")
    match opcion:
        case '1':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            print(f"La suma es: {suma(numUno, numDos)}")
        case '2':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            print(f"La resta es: {resta(numUno, numDos)}")
        case '3':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            print(f"La multiplicacion es: {multiplicacion(numUno, numDos)}")
        case '4':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            print(f"La division es: {division(numUno, numDos)}")
        case '5':
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            print(f"La potencia es: {potencia(base, exponente)}")
        case '6':
            num = float(input("Ingrese el numero: "))
            print(f"La raiz cuadrada es: {raiz_cuadrada(num)}")
        case '7':
            angulo = float(input("Ingrese el angulo en grados: "))
            print(f"El seno es: {seno(angulo)}")
        case '8':
            angulo = float(input("Ingrese el angulo en grados: "))
            print(f"El coseno es: {coseno(angulo)}")
        case '9':
            angulo = float(input("Ingrese el angulo en grados: "))
            print(f"La tangente es: {tangente(angulo)}")
        case '10':
            num = float(input("Ingrese el numero: "))
            base = float(input("Ingrese la base: "))
            print(f"El logaritmo es: {logaritmo(num, base)}")
        case '11':
            print("Saliendo del programa.")
            break