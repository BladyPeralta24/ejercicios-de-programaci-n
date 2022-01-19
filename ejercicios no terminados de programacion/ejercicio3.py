Diccionario = {}
salir = 0
while salir != '':
    if salir != '':
        nombre = input("Introduzca el nombre:")
        edad = input("Introduzca la edad: ")
        sexo = input("Introduzca el sexo: ")
        telefono = input("Introduzca su numero de telefono: ")
        email = input("Introduzca su email: ")

        Diccionario.setdefault(nombre, {"edad": edad, "sexo": sexo, "Telefono": telefono, "Email": email})
        print (Diccionario)