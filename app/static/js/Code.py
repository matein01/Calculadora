"""Libreria math para las operaciones matematicas avanzadas"""
import math

"""Creación de la cola"""
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
    
"""Creación de la fila"""
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

"""Funcion para sumar"""
def suma(numUno, numDos):
    resultado = numUno + numDos
    return resultado

"""Funcion para restar"""
def resta(numUno, numDos):
    return numUno - numDos

"""Funcion para multiplicar"""
def multiplicacion(numUno, numDos):
    return numUno * numDos

"""Funcion para dividir"""
def division(numUno, numDos):
    if numDos == 0:
        return "Error: Division by zero"
    return numUno / numDos

"""Funcion para calcular la potencia"""
def potencia(base, exponente):
    return math.pow(base, exponente)

"""Funcion para calcular la raiz cuadrada"""
def raiz_cuadrada(num):
    if num < 0:
        return "Error: Negative input for square root"
    return math.sqrt(num)

"""Funcion para calcular el angulo de seno"""
def seno(angulo):
    return math.sin(math.radians(angulo))

"""Funcion para calcular el angulo de coseno"""
def coseno(angulo):
    return math.cos(math.radians(angulo))

"""Funcion para calcular el angulo de la tangente"""
def tangente(angulo):
    return math.tan(math.radians(angulo))

"""Funcion para calcular un logaritmo"""
def logaritmo(num, base):
    if num <= 0:
        return "Error: Non-positive input for logarithm"
    if base <= 1:
        return "Error: Logarithm base must be greater than 1"
    return math.log(num, base)

"""Creacion de estucturas de datos"""
fila = Fila()
cola = Cola()
lista = []

"""Manejo de bucle while para la funcionalidad de la calculadora hasta que el usuario lo decida."""
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
    """Condicionales para que el menu funcione segun la opcion que elija el usuario"""
    match opcion:
        case '1':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = suma(numUno, numDos)
            print(f"La suma es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '2':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = resta(numUno, numDos)
            print(f"La resta es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '3':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = multiplicacion(numUno, numDos)
            print(f"La multiplicacion es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '4':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            numUno = float(input("Ingrese el primer numero: "))
            numDos = float(input("Ingrese el segundo numero: "))
            resultado = division(numUno, numDos)
            print(f"La division es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '5':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            resultado = potencia(base, exponente)
            print(f"La potencia es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '6':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            num = float(input("Ingrese el numero: "))
            resultado = raiz_cuadrada(num)
            print(f"La raiz cuadrada es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '7':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            angulo = float(input("Ingrese el angulo en grados: "))
            resultado = seno(angulo)
            print(f"El seno es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '8':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            angulo = float(input("Ingrese el angulo en grados: "))
            resultado = coseno(angulo)
            print(f"El coseno es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '9':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            angulo = float(input("Ingrese el angulo en grados: "))
            resultado = tangente(angulo)
            print(f"La tangente es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '10':
            """Se piden dos numeros y se convierten a decimales, luego se llama a la funcion y el resultado se guarda en una variable que se muestra en pantalla mientras se guarda en todas las estructuras de datos"""
            num = float(input("Ingrese el numero: "))
            base = float(input("Ingrese la base: "))
            resultado = logaritmo(num, base)
            print(f"El logaritmo es: {resultado}")
            fila.agregar(resultado)
            cola.agregar(resultado)
            lista.append(resultado)
        case '11':
            """Se crea un nuevo bucle para que usuario pueda ver todas las estructuras de datos y luego finalizar el programa, o no revisar ninguna"""
            while True:
                print("Selecciona una estructura de datos")
                print("1. Para la lista completa")
                print("2. Para ver la fila (Ultimo valor)")
                print("3. Para ver la cola (Primer valor valor)")
                print("4. No ver resultados")
                opcion = input("Ingrese su opcion (1-4): ")
                """Se crea una estructura de condiciones para que haya un control al momento de mostrar las listas"""
                match opcion:
                  case '1':
                        """Se imprimen todos los resultados guardados en la lista, ademas que da la opcion de eliminar los resultados que el usuario desee"""
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
                        """Se imprime la fila y se da la opcion de eliminar el elemento mostrado en pantalla"""
                        print(f"El ultimo resultado original es: {fila.mostrar()}")
                        print("Deseas eliminar el resultado de la fila?")
                        eliminar = input("1. Si 2. No: ")
                        if eliminar == '1':
                            eliminado = fila.mostrar()
                            print(f"El resultado {eliminado} ha sido eliminado")
                        print(f"El ultimo resultado actual es: {fila.mostrar()}")
                  case '3':
                        """Se imprime la cola y se da la opcion de eliminar el elemento mostrado en pantalla"""
                        print(f"El primer resultado original es: {cola.mostrar()}")
                        print("Deseas eliminar el resultado de la cola?")
                        eliminar = input("1. Si 2. No: ")
                        if eliminar == '1':
                            eliminado = cola.mostrar()
                            print(f"El resultado {eliminado} ha sido eliminado")
                        print(f"El primer resultado actual es: {cola.mostrar()}")
                  case '4':
                        """Se finalizan ambos bucles"""
                        print("No se veran resultados")
                        print("Saliendo...")
                        break
            break