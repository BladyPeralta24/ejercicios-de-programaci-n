#Diccionario de una fruteria
productos={'Platano' : 1.35, 'Manzana' : 0.80, 'Pera' : 0.85, 'Naranja' : 0.70}

fruta=str(input("Elije una fruta de la tabla, por favor: "))
kilos=input("¿Cuantos kilos deseas obtener?: ")

#En el caso de que la fruta no este en la lista, poner un aviso

if not productos[fruta]:
    print("Lo sentimos, esta fruta no esta en la tabla")
else:
    precio=
