'''
palabra = 'por'
print(len(palabra))

vacio = ''
print(len(vacio))

yo_soy = 'I\'m'
print(len(yo_soy))

multlinea = ''''''linea #1
linea #2'''
'''
print(len(multlinea))
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


ch1 = "@"
ch2 = '' #espacio
ch3 = "["

print(ord(ch1))
print(ord(ch2))
print(ord (ch3))

print (chr(64))
print(chr(945))


alpha = "abcdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[::2])
print(alpha[::3])
print(alpha[1::2])

alpfabeto ="abcdefghijklmnopqrstuvwyz"
print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("xyz" in alpfabeto)

alpfabeto = "bcdefghijklmnopqrstuvwxy"
alpfabeto = "a" + alpfabeto
alpfabeto = alpfabeto + "z"

print(alpfabeto)

print(min("aAbByYzZ"))
t=[0.1,2]
print(min(t))

print(max("aAbByYzZ"))

t= 'Los Caballeros Que Dicen "¡Ni!"' 
print('['+ max(t)+']')
t=[0,1,2]
print(max(t))
'''

print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

print(list("abcabc"))


print("abcabc".count("b"))
print('abcabc'.count("d"))

print('aBcD'.capitalize())

print('['+ 'Beta'.center(2)+']')
print('['+ 'Beta'.center(8)+']')
print('['+ 'Beta'.center(12)+']')

print('['+ 'gamma'.center(20)+']')

t="zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

print("omega".startswith("meg"))
print("omega".startswith("om"))
t='alfabeto'

print(t.find('eto'))
print(t.find('et'))
print(t.find('fa'))
print(t.find('a'))

print('lamdba30'.isalnum())
print('lamdba'.isalnum())
print('30'.isalnum())
print('lamdba_30'.isalnum())
print(''.isalnum())


print("Mooooo".islower())
print('moooo'.islower())
print("________________")


print('\n'.isspace())
print("".isspace())
print("______________".isspace())




print("SiGmA=60".lower())


print("wwww.netacad.com".replace("netacad.com","pythoninstitute.org"))
print("This is it!".replace("is","are"))
print("Apple juice".replace("Juice",""))




print("Hugo                         Alexander Peña".split())

print("Yo se que no se nada".swapcase())
print()

print("Yo se que no se nada. parte 1".title())

print("Yo se que no se nada. parte 2".upper())


secondgreek = ['omega', 'alfa', 'pi', 'gama']
print(secondgreek)

secondgreek.sort()
print(secondgreek)


