dni=""
while not(dni.isnumeric()) or len(dni)!=8:
    dni=input("Introduce el dni, por favor: ")
letra="TRWAGMYFPDXBNJZSQVHLCKE"
resto=int(dni)%23
print("Su dni es valido y tiene la letra: ",letra[resto])