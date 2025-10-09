import math
""" from flask import Flask

app = Flask (__name__)
 """

class Cola:
    def __init__(self):
        self.cola = []

    def agregar(self, item):
        self.cola.append(item)

    def vacio(self):
        return len(self.cola)==0

    def mostrar(self):
        if not self.vacia():
            return self.cola.pop(0)
    
class Fila:
    def __init__(self):
        self.fila = []

    def agregar(self, item):
        self.fila.append(item)

    def vacio(self):
        return len(self.fila)==0

    def mostrar(self):
        if not self.vacia():
            return self.fila.pop(-1)

def suma(numUno, numDos):
    resultado = numUno + numDos
    return resultado

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

fila = Fila()
cola = Cola()
lista = []

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
            resultado = suma(numUno, numDos)
            print(f"La suma es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '2':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = resta(numUno, numDos)
            print(f"La resta es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '3':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = multiplicacion(numUno, numDos)
            print(f"La multiplicacion es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '4':
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = division(numUno, numDos)
            print(f"La division es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '5':
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            resultado = potencia(base, exponente)
            print(f"La potencia es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '6':
            num = float(input("Ingrese el numero: "))
            resultado = raiz_cuadrada(num)
            print(f"La raiz cuadrada es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '7':
            angulo = float(input("Ingrese el angulo en grados: "))
            resultado = seno(angulo)
            print(f"El seno es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '8':
            angulo = float(input("Ingrese el angulo en grados: "))
            resultado = coseno(angulo)
            print(f"El coseno es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '9':
            angulo = float(input("Ingrese el angulo en grados: "))
            resultado = tangente(angulo)
            print(f"La tangente es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '10':
            num = float(input("Ingrese el numero: "))
            base = float(input("Ingrese la base: "))
            resultado = logaritmo(num, base)
            print(f"El logaritmo es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '11':
            print("Saliendo del programa.")
            print(f"Estos fueron tus resultados: {lista}")
            # print(f"La fila es {fila.mostrar()}")
            # print(f"La cola es {cola.mostrar()}")
            break