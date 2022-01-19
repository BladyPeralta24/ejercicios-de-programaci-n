#Producto vectorial
a=['i','j','k']
b=['i','j','k']
resultado = ['i','j','k']


a[0] = int(input("Introduzca el valor i del vector a: "))
a[1] = int(input("Introduzca el valor j del vector a: "))
a[2] = int(input("Introduzca el valor k del vector a: "))
print(a[0],'i,',a[1],'j,',a[2],'k,')
b[0] = int(input("Introduzca el valor i del vector b: "))
b[1] = int(input("Introduzca el valor j del vector b: "))
b[2] = int(input("Introduzca el valor k del vector b: "))
print(b[0],'i,',b[1],'j,',b[2],'k,')

resultado[0]=a[1]*b[2]-a[2]*b[1]
resultado[1]=a[2]*b[0]-a[0]*b[2]
resultado[2]=a[1]*b[0]-a[0]*b[1]
print(resultado[0],'i,',resultado[1],'j,',resultado[2],'k,')


