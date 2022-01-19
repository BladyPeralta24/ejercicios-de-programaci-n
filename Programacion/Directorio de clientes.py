# [Diccionario] Directorio de clientes 
cadena ="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Usuario = {}

for linea in cadena.split("\n")[1: ]:
    dato = linea.split(';')
    nif = dato [0]
    nombre = dato [1]
    apellido = dato [2]
    Usuario.setdefault(nif, {"nombre": nombre, "apellido": apellido})

print (Usuario)



