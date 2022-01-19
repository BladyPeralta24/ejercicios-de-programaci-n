lista = []

#Introducir numeros a la lista
num_ganador= 0
i = 0
while i < 15 and num_ganador != '':
    num_ganador = input("Escribe el numero ganador, por favor: ")
    if num_ganador != '' and num_ganador.isnumeric():
        lista.append(int(num_ganador))
        print(lista)
        i+=1
        


#Ordenar lista
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista [j] > lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

complementario = str(input("Introduzca el complementario: "))
reintegro = str(input("Introduzca el reintegro: "))
print ("Los números ganadores son:\n",lista, " \nComplementario:",complementario, " \nReintegro:",reintegro)