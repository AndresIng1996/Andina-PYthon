'''
print(6/0)

lista = []
x = lista[0]



Primernumero = int(input("ingrese el primer numero:")) 
segundonumero = int(input("ingrese el primer segundo:"))

if segundonumero!=0:
    print(Primernumero/segundonumero)
else:
    print("Esta operacion no puede ser realizada.")

#sopechas de errores se hace necesario utilizar el try
try:
    print("todo va bien ")
    x= 1 /1
    print("sigue bien")
except:
    print("oh cielos, algo salio mal...")

try:
    x= int(input("ingresa un numero:"))
    y=1/x
    print(y)
except:
    print("oh cielos, algo salio mal...")

print("FIN.")

try:
    x = int(input("ingresa un numero:"))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("oh cielos, algo salio mal...")
except ValueError:
    print("Debes ingresar un valor entero.")
    print("THE END.")

try:
    x= int(input("ingrese numero:"))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")
    print("FIN")

try:
    x= int(input("ingrese numero:"))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
print("FIN")



import math
x = float(input("Ingrese un numero:"))
assert x>=1

x= math.sqrt(x)
print(x)

x = input("Ingrese su nombre")
print("¡Hola" + x + "!")


x = ((3*3)/2.5)**2
print(x)

num1 = int(input("Ingrese numero:"))
num2 = int(input("ingrese numero:"))
div = num1 // num2
residuo= num1%num2
print("el dividendo es:",num1,"el divisor es", num2)
print("el resultado de la divion es:", div)
print("el residuo es:", residuo)

Asignaturas = ["Matematicas", "Fisica","Quimica","Historia","Lengua"]
for Asignatura in Asignaturas:
    print("Yo estudio", Asignatura)

Asignaturas = ["Matematicas", "Fisica","Quimica","Historia","Lengua"]
scores=[]
for Asignatura in Asignaturas:
    scores = input("¿Que nota has sacado en"+ Asignatura+"?")
    scores.append(scores)
for i in range(len(Asignaturas)):
    print("En"+ Asignaturas[i]+",")
  
loteri= []
for i in range(5):
    numero =int (input("Digitar el numero"+ str(i) + " de la loteria"))
    loteri.append(numero)

print("Los numero de la loteria son:", loteri.sort()) 

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
  

key= "contraseña"
password = input("introduce ña contraseña:")
if key== password.lower():
        print("la contraseña conincide")
else:
        print("la contraseña no incide")

num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese un numero"))


try:
    div = num1 / num2
except ZeroDivisionError:
    print(" no se puede dividir")

edad = int(input("introduce tu edad:"))
if edad< 4:
    precio = 0
elif edad <= 18:
    precio =4
else:
    precio=10

print("El precio de la entrega es", precio, "E.")

nombre = input(("nombre"))
edad = input(("edad"))
direccion = input(("direccion"))
telefono = input("telefono")
persona = {'nombre':nombre,
'edad':edad,
'direccion':direccion,
'telefono':telefono}
print(persona['nombre'],'tiene',persona['edad'],'años,vive en',persona['direccion','y su numero de telefono es',persona['telefono']])

'''
def invoce(amount, iva=16):
    return amount + amount*iva/100

print(invoce(1000/10))
print(invoce(1000))


