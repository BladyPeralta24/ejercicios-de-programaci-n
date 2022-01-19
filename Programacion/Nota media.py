lista_modulos = []
notas = 0
posicion = 0
modulos = 1

while modulos !='':
    modulos = input("Introduzca los modulos, de lo contrario pulsa enter: ")
    if modulos !='':
        lista_modulos.append(modulos)
print(lista_modulos[:])

for modulo in lista_modulos:
    notas += int(input("¿Qué nota has sacado en "+modulos+"?: "))

nota_media = notas/len(lista_modulos)
print("Su nota media en los modulos es:",nota_media)
