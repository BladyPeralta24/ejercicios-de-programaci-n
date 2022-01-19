class Persona:

    def __init__(self, nombre="", edad=18, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni


    def mostrar(self):
        return "Nombre : " + self.__nombre + "\nEdad : " + str(self.__edad) + "\nDNI : " +str(self.__dni)
    
    def esMayorDeEdad(self):
        return self.__edad >= 18
           

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int):
            self.__edad = nueva_edad
        else:
            print("El formato de la edad, no es valido")

    @property
    def dni(self):
        return self.__dni
    
    def validarNIF(self,nif):
        letra = nif[-1:].upper()
        dni = int(nif[0:8])
        restoLetra = dni % 23
        comprobacion = "TRWAGMYFPDXBNJZSQVHLCKE"

        if comprobacion[restoLetra] == letra: #buscar un elemento en una cadena mediante una posicion
            return True
        else: 
            return False
    
    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni


            

    
    
persona1 = Persona()

persona1.nombre = "Juan"
persona1.edad = 30
persona1.dni = "56987463"

print(persona1.mostrar())
print(persona1.esMayorDeEdad())