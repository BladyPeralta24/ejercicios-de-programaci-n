que el usuario inserte una fecha en formato aaaammdd, que nos devuelva verdadero o falso si entra en febrero de 2020

imprimir ("introduce una fecha(en formato aaaammdd)")
f=leer()
año=f[0,3]
mes=f[4,5]
dia=f[6,7]
    Si año="2020" y mes = "02" entonces
            imprimir ("La fecha es valida")
        Sino
            imprimir ("No coincide con la fecha dada")
        Fin si


otra alternativa
imprimir ("introduce una fecha(en formato aaaammdd)")
f=leer()
si f[0,5]="202002" entonces
    imprimir ("La fecha es valida")
si no
    imprimir ("No coincide con la fecha dada")
Fin si
