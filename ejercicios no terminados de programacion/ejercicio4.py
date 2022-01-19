# Pedir al usuario un numero entero
# De ese numero que se muestre por pantalla un triangulo 
# con altura igual al numero introducido


num = int(input ("Introduce un número: "))

print (num)

i = 0
asterisco = '*'
while i <= num:
    #print(i)
    print (asterisco * i)
    i+=1


