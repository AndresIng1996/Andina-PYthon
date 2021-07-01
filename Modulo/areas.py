def areacuadrado():
    lado = int(input("Ingrese el valor del lado "))
    return print("el area del cuadrado es:", lado**2)


def arearectangulo():
    base = int(input("Ingrese el valor del la base "))
    altura = int(input("Ingrese el valor de la altura "))
    return print("el area del rectandulo es:", base * altura)

def areacirculo():
    radio= int(input("Ingrese el valor del radio "))
    __pi = 3.1416
    return print("el area del circulo es:", __pi * (radio**2))

if __name__==("__main__"):
    print(" estoy en la funcion principal")
    areacirculo()
    areacuadrado()
    arearectangulo()
else:
    print(" en  este momento me comporto como un mdulo")
    print(__name__)
    