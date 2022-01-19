'''Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 

Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y valor será otro diccionario formado por pares de clave/valor del tipo modulo/nota (entero).

Al final el programa nos mostrará el diccionario de alumnos y la nota media obtenida por cada uno de ellos. 

Obtener:
{
    'Juan Fransisco : {
        'Programación' : 6
       ,'Redes' : 4
    }
    ,'Andrés': {
        'Lenguaje de marcas' : 7
       ,'Matemáticas' : 3
    }

}


Resultado:
{
    'Juan Fransisco : 5
    ,'Andrés': 5
}'''


alumno = {}
calificacion = {}
dic_modulo_nota = {}
nota_media = 0

nombre = input("Nombre: ")

cantidad = int(input("cuantos módulos participa "+nombre+ ": "))


while cantidad > 0:
    
    modulo = input("Módulo: ")

    nota = input("Nota en "+modulo+ ": ")

    nota_media = int((nota_media + nota) / cantidad)

    dic_modulo_nota.setdefault(modulo,nota)
        
    cantidad -= 1

alumno.setdefault(nombre, dic_modulo_nota)

print(alumno)


calificacion.setdefault(nombre, nota_media)

print (calificacion)


