#Un algoritmo, que solicite al usuario 100 valores(5 de prueba), y al final imprima que valor es el mayor introducido y cual es el menor

i = 0
while i< 5 :
    n1=input("Introduce un número: ")
    i +=1
    max = n1
    min = n1
    if max>n1 :
        max = n1
    elif min<n1:
        min = n1
print ("El número maximo es:",max)
print("El número minimo es:",min)