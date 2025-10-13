import math

class Cola:
    def __init__(self):
        self.cola = []

    def agregar(self, item):
        self.cola.append(item)

    def vacio(self):
        return len(self.cola)==0

    def mostrar(self):
        if not self.vacio():
            return self.cola.pop(0)
    
class Fila:
    def __init__(self):
        self.fila = []

    def agregar(self, item):
        self.fila.append(item)

    def vacio(self):
        return len(self.fila)==0

    def mostrar(self):
        if not self.vacio():
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
    print("11. Ver resultados")
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
            while True:
                print("Selecciona una estructura de datos")
                print("1. Para la lista completa")
                print("2. Para ver la fila (Ultimo valor)")
                print("3. Para ver la cola (Primer valor valor)")
                print("4. No ver resultados")
                opcion = input("Ingrese su opcion (1-4): ")
                match opcion:
                  case '1':
                        cantidad = len(lista)
                        print(f"El total de resultados es: {cantidad}")
                        print(f"La lista de todos los resultados es:")
                        for i in range(0,cantidad):
                            print(lista[i])
                        print("Deseas eliminar algun resultado?")
                        eliminar = input("1. Si 2. No: ")
                        if eliminar == '1':
                            print(f"Selecciona el numero que deseas eliminar (1-{cantidad}): ")
                            numEliminar = int(input())
                            numEliminar = numEliminar - 1
                            eliminado = lista.pop(numEliminar)
                            print(f"El resultado {eliminado} ha sido eliminado")
                            print("La lista actualizada es:")
                            cantidad = len(lista)
                            for i in range(0,cantidad):
                              print(lista[i])
                  case '2':
                        print(f"El ultimo resultado original es: {fila.mostrar()}")
                        print("Deseas eliminar el resultado de la fila?")
                        eliminar = input("1. Si 2. No: ")
                        if eliminar == '1':
                            eliminado = fila.mostrar()
                            print(f"El resultado {eliminado} ha sido eliminado")
                        print(f"El ultimo resultado actual es: {fila.mostrar()}")
                  case '3':
                        print(f"El primer resultado original es: {cola.mostrar()}")
                        print("Deseas eliminar el resultado de la cola?")
                        eliminar = input("1. Si 2. No: ")
                        if eliminar == '1':
                            eliminado = cola.mostrar()
                            print(f"El resultado {eliminado} ha sido eliminado")
                        print(f"El primer resultado actual es: {cola.mostrar()}")
                  case '4':
                        print("No se veran resultados")
                        print("Saliendo...")
                        break
            break