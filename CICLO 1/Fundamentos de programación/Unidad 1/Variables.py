# Ejemplo uno Comentario de una sola linea
'''
var = "3.7.1" 
print(var)
print ("el tipo de la variable es: ", type(var))
print()#salto de linea
var = 1.2
print(var)
print ("el tipo de la variable es: ", type(var))
print()#salto de linea
var = var + 1
print(var)
print ("el tipo de la variable es: ", type(var))
print()#salto de linea
var = 100
print(var)
print ("el tipo de la variable es: ", type(var))
print()#salto de linea
var = 200 + 300
print(var)
print ("el tipo de la variable es: ", type(var))
print()#salto de linea
var1 = 1
var2=var1
print(var2, var1) # puedo imprimir dos valores en el mismo print
'''

'''Comentario de una seccion inicia con tres comillas y se cierra de la misma manera'''
'''
#Realizar procesos de multiplicacion y acumularlos en la misma variable
x = 1
x = x * 2
print(x)
x = 1
x *= 2
print(x)# Su resultado es igual a la operacion anterior debido a que en la linea 33 x=1, borre el resultado anterior y se establecio en 1
x *= 2
print(x)# Da un resultado diferente ya que deje a x con el valor anterior es decir 2
#Realizar procesos de suma y acumularlos en la misma variable
oveja=25
oveja=oveja+1
print(oveja)
oveja+=1
print(oveja)
'''

'''
#y si se acumula mas de dos variables, esposible?
i=1
j=2
i=i+2*j
i+=2*j
print(i,j)
'''
'''
#Para division
var=100
var=var/2
print(var)#Division con valor decimal
var/=2
print(var)
'''
'''
rem=5
rem=rem%10 #Modulo selecciona el primer argumento y lo divide entre el segundo, devuelve el residuo
print(rem) # Devuelve 5 por que el numero es mayor a 5, asi se empieza con decimal
rem%=10
print(rem) 
# si es 10 rem que pasa
'''
'''
rem=10
rem=rem%10 #Modulo selecciona el primer argumento y lo divide entre el segundo, devuelve el residuo
print(rem) # Devuelve 5 por que el numero es mayor a 5, asi se empieza con decimal
rem%=10
print(rem) 
'''

'''
j=50
x=100
var=55
rem=99
i=65
j=j-(i+var+rem) # Parentesis nos ayudan a generar procesos mas claros a la hora de realizar una operacion
print(j)
j-=(i+var+rem)
print(j)
x=x**2 #potencia x^2
print(x)
x**=2
print(x)
'''

'''
#Error de variables

#var 1 = 120
var1 = 120
#@var1 = 120 # recordar que el @ no esta permitido
#1var = 120
#var-1 = 120
var_1 = 120
'''

#Asignación entre variables
'''
var1, var2, var3 = 1, 2, 3 #Asignacion entre variables
print("La variable var1 es: ", var1)
print("La variable var2 es: ",var2)
print("La variable var3 es: ",var3)
var1, var2, var3 = var3, var2, var1
print("La variable var1 es: ",var1)
print("La variable var2 es: ",var2)
print("La variable var3 es: ",var3)
var1 = var2 = var3 = 200
print(var1, var2, var3)
'''

#Para definir un float (decimal), se usa la siguiente sintaxis:
'''
mientero = 1
print(mientero)
print(type(mientero))
'''

#Para definir un float (decimal), se usa la siguiente sintaxis:
'''
mifloat = 1.0
print(mifloat)
print(type(mifloat))
'''

''' Precedencia, la convención matemática. 
PEMDAS 
    Parentesis
    Exponencial
    Multiplicacion, Division
    Suma, Resta
'''
'''
x = 2 * (5 - 1)# se realiza por , primero hace 5-1= depues se multiplica por dos
print("Precedencia entre los parentesis: ",x)
y = (1 + 1) ** (5 - 2)# 2^3
print("Precedencia entre los parentesis, aplicado a potencia: ",y)
x=2 ** 1 + 1# 2^1 + 1=3
print("Precedencia sin parentesis: ",x)
y = 3 * 1 ** 3 # 1^3 despues multiplica por 3
print("Precedencia sin parentesis: ",y)
x = 2 * 3 - 1
print("Precedencia sin parentesis: ",x)
'''
#Promedio de Variables
'''
var1 = 1.0
var2 = 4.5
var3 = 5.5
var4 = 2.5
promedio = (var1 + var2 + var3 + var4)/4
print(promedio)
print("El promedio de esos números es "+str(promedio)) # se especifica que el dato promedio es un texto por eso
                                                        #no esta la coma, el + es de union concatenar
print("El promedio de esos números es ", round(promedio))# rendodea sin tener cifras significativas
print("El promedio de esos números es ", round(promedio, 2))# rendodea a dos cifras significativas
'''

#Calcule el área y perímetro de un cuadrado Formulas:
'''
lado = 10
area = lado * lado
perimetro = lado + lado + lado + lado
print(lado)
print(perimetro)
print(area)'''
