n1 = 0
n2 = 1
i = 0
while i < 15:
    print (n1, end= " - ")
    aux = n1 + n2
    n1 = n2
    n2 = aux
    i += 1
print ("Fibonacci")

# otra alternativa


a = 0
b = 1

i = 0


while i < 15:
    print (str(a) + " - ", end="")
    print (str(b) + " - ", end="")
    
    a = a + b
    b = a + b

    i += 2