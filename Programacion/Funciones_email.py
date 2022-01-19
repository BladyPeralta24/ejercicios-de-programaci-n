

# El usuario introduce el email: cascaradenaranja@hotmail.com o vivalavida@gmail.es
# para que el email sea valido, tengo que localizar el '@' y el '.com' o '.es'
# para ello tenemos que usar un find para localizar esos caracteres
# si lo localiza, devolvera true, sino devolvera false

# nota: el email tiene que estar ordenado, no vale de que este el .com antes que @
# no seria válido 
# email de prueba: cascaradenaranja@hotmail.com
email=input("Introduce tu email, por favor: ")
def ValidarEmail(email):
    if email == email.find("@"):
    else:
        return False



print (ValidarEmail(email))




'''if ValidarEmail(email):
    print("email valido")
else:
    print("email no valido")'''
