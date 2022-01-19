 que solicita al usuario una fecha de inicio y fin y luego una tercera fecha 
 y nos devuelva que si la tercera fecha en anterior, medio o posterior a las otras fechas 
 formato:dd/mm/aaaa

 imprimir ("introduce la primera fecha")
 fecha1=leer()
 imprimir ("introduce la segunda fecha")
 fecha2=leer()
 imprimir ("introduce la tercera fecha")
 fecha3=leer()

 f1= (fecha1[6,9](int) + fecha1[3,4](int) + fecha1[0,1](int))(imt)
 f2= (fecha2[6,9](int) + fecha2[3,4](int) + fecha2[0,1](int))(int)
 f3= (fecha3[6,9](int) + fecha3[3,4](int) + fecha3[0,1](int))(int)
Mientras f3 =! f1 y f3 =! f2 hacer
  si f3 < f1 entonces
    imprimir ("la fecha es menor que el tramo")
  sino
    si f3>f1 y f3<f1 entonces
      imprimir ("la fecha esta en medio del tramo")
    sino
      si f3>f2 entonces
        imprimir("la fecha es mayor del tramo")
      fin si
    fin si
  fin si
Fin Mientras


