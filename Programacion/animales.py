animales_lista = ["Perro", "Gato", "Elefante", "Girafa"]

#animal=input("Introduzaca un animal en la lista, por favor: ")
#animales.append(animal)
#print(animales)
i=1
while i != 1:
    animal=input("Introduzaca un animal en la lista, por favor: ")
    animales_lista.append(animal)
    print(animales_lista)
    if animal == animales_lista["Perro"]:
         animales_lista.remove(animal)