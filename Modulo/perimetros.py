def percuadrado():
    lado = int(input("Ingrese el valor del lado "))
    return print("el perimetro del cuadrado es:", 4*lado)



def perrectangulo():
    base = int(input("Ingrese el valor del la base "))
    altura = int(input("Ingrese el valor de la altura "))
    return print("el perimetro del rectandulo es:", (2*base)+ (2* altura))


def percirculo():
    radio= int(input("Ingrese el valor del radio "))
    __pi = 3.1416
    return print("el area del circulo es:", 2*__pi*radio)


if __name__==("__main__"):
    print(" estoy en la funcion principal")
    percirculo()
    percuadrado()
    perrectangulo
    print(__name__)

else:
    print(" en  este momento me comporto como un mdulo")
    print(__name__)