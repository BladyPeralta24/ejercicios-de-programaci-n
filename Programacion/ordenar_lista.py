#Lista ordenada
lista = []
elemento_nuevo = 0
while elemento_nuevo != '':
    elemento_nuevo = input("Introduce un valor entero a la lista: ")

    if elemento_nuevo != '' and elemento_nuevo.isnumeric():
        lista.append(int(elemento_nuevo))

#Lista completa


for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j] > lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print (lista)
