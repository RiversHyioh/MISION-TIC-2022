'''
print() = Imprime por consola
int() = define un valor entero
type() = imprime el tipo de valor
round() = redondea numero con decimal o establece numero máximo de decimales
max() = selecciona mayor valor de lista
min() = selecciona menor valor de lista
help() = ayuda sobre palabra reservada
sum() = suma un rango de valores
range() = establece un rango
return() = devuelve argumentos
'''

# Max Min
'''
numeros = [25, 26, 25, 24]# lista [] almacena elementos del mismo tipo, numeros, strings
maximo = max(numeros)
print(maximo)
minimo = min(numeros)
print(minimo)
suma = sum(numeros)
print(suma)
'''
'''
# Help
help(print)
# help(max)
# help(min)
# help(type)
'''

#Ejemplo uno de funciones
'''
def imprime_Cosas():
    print("La clase esta genial")
    print('Python es lo máximo')

imprime_Cosas()

def repetir_funciones():
    print("\n")
imprime_Cosas()
imprime_Cosas()
repetir_funciones()


#Ejemplo dos de funciones

def repetir_funciones():
    print("\n")
    imprime_Cosas()
    imprime_Cosas()

repetir_funciones()

def imprime_Cosas():
    print("La clase esta genial")
    print('Python es lo máximo')

imprime_Cosas()
'''

#Ejemplo tres de funciones
'''
def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1: "))# input aloja el argumento como string
    num2 = float(input("Ingrese el numero 2: "))
    print("la suma de", int(num1), " + ", int(num2), " es igual a: ", int(num1 + num2))#aunque estan dado el dato y quede como flotante 
                                                    #el resultado esta estipuladoa como entero

sumarDosnumeros()
'''
#Ejemplo cuatro de funciones
'''
def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcaluar su raiz cuadrada: "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada de : ", valor, " es ", valor ** 0.5)

raizCuadrada()
'''
#Argumentos y parámetros
# Enviar argumentos a un función
# Ejemplo uno
''' 
def suma(a, b):
    return a + b

print(suma(30, 10))'''

#Ejemplo dos
'''
def suma(a, b):
    return a + b

b = 30 #Se le asigna el valor y depues se pasa a la funcion, no importa el orden de asignacion
            #solo como se llama al proceso de la funcion
a = 10
print(suma(a, b))
'''

#Sentencia return
#Ejemplo 1
'''
def otra_suma(numero1, numero2):

    print(numero1 + numero2)
    print()
    # a=numero1 + numero2 #con esto se soluciona cuando da none
    # return a

resultado = otra_suma(5,6)

print(resultado)
'''

#Ejemplo 2
'''
def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2
otra_suma(5, 6)
'''

#Parámetro valor que la función espera recibir cuando sea llamada
#Ejemplo 1
'''
def mi_funcion(nombre, apellido):
    miNombre = nombre + apellido
    return(miNombre)

print(mi_funcion("Ana ", "Tamayo"))
'''

#Ejemplo 2 Omision
'''
def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)

saludar('Pepe Grillo')
'''

#Funciones dentro de otra función
#Ejemplo1
'''
#Primera función
def imprime_Cosas():
    print("La clase esta genial")
    print('Python es lo máximo')

imprime_Cosas() # Llamado a la primera funcion
print("\n")

#segunda función
def repetir_funciones():
    imprime_Cosas()# Llama a la funcion por primera vez
    imprime_Cosas()# llama a la funcion por segunda vez

repetir_funciones()# se tienen dos llamados de la funcion inicial
'''

#Ejemplo 2
'''
def mensaje():
    print("Ingrese por favor un valor")

def sumarDosnumeros():
    mensaje()
    num1 = float(input())
    mensaje()
    num2 = float(input())
    return print("la suma de ",num1, " + ", num2, " es igual a: ", num1 + num2)

sumarDosnumeros()
'''

#Ejemplo 3
'''
def mensaje():
    print("Por favor, Introduzca un numero a calcaluar su raiz cuadrada: ")

def raizCuadrada():
    mensaje()
    valor = float(input())
    raiz = valor ** 0.5
    return print("La raiz cuadrada de : ", valor, " es ", valor ** 0.5)

raizCuadrada()
'''

# Funciones Anidadas
#Ejemplo uno
'''
def primeraFuncion(): # función externa
    print ("\n \"Hola desde la función externa\" \n ")
    print ("Hola desde la función externa")
    def segundaFuncion(): # función interna
        print ("\n \"Hola desde la función interna\" \n")
        print ("Hola desde la función interna")
    segundaFuncion()
primeraFuncion()
'''
'''
#Ejemplo dos

def primerNumero(x):
    def segundoNumero(y):
        return x ** y
    return segundoNumero
print(primerNumero(2))
resultado = primerNumero(2) #hago la asignacion de la primera funcion x
print(resultado)
print(resultado(5))  # se hace la asignacion de la segunda funcion y

#print(segundoNumero(2)) #es error por que no esta definida, recordar que solo se puede acceder por primerNumero
'''
