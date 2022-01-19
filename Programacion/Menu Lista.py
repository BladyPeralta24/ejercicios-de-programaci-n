# Paso 1: Código para introducir valores en la lista
lista = []
contenido = 0
num = 0

while contenido != "":
    contenido = input("Introduce palabras en la lista, de lo contrario pulsa Enter: ")

    if contenido != "":
        lista.append(str(contenido))

print (lista[:])

#paso 2: crear una funcion para el menu
def PedirLetra():

    cierto=False
    letra=0
    while(not cierto):
        try:
            letra = str(input("Introduce una letra: "))
            cierto=True
        except ValueError:
            print("Error, introduce una letra del menu, por favor: ")

    return letra

salir = False
opcion = 0
#Paso 3: introducir un menu para el usuario
while not salir:
    print("Elige una de estas opciones:")
    print("[C] Contar")
    print("[M] Modificar")
    print("[E] Eliminar")
    print("[S] Mostrar")
    print("[T] Terminar")

    opcion = PedirLetra()

    if opcion == 'c':
        contar=str(input("Introduce una palabra que quieres buscar: "))
        num= lista.count(contar)
        print("la palabra " ,contar, " aparece" ,num, " veces")

    elif opcion == 'm':
        print ("modificar")

    elif opcion == 'e':
        print ("eliminar")

    elif opcion == 's':
        print (lista[:])

    elif opcion == 't':
        #print ("terminar")
        salir = True

    else:
        print ("Introduce solo las letras que estan en el menu")

print ("Fin del porgrama :)")
    




