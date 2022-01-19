

nif = input("Introduce el nif, por favor: ")
def ValidarNIF(nif):
    letra="TRWAGMYFPDXBNJZSQVHLCKE"
    resto=int(nif[0:8])%23

    if  nif[0:8].isnumeric() and len(nif)==9 and letra[resto] == nif[8]:
        return True
    else:
        return False

 
 
if ValidarNIF(nif):
    print("El nif es válido")
else:
    print ("El nif es inválido")
 
