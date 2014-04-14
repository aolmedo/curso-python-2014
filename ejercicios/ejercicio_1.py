#def ejercicio_1():
a = raw_input("Ingrese un numero: ")
b = raw_input("Ingrese otro numero: ")
c = raw_input("Ingrese otro numero: ")
a = int(a)
b = int(b)
c = int(c)

ret = a
if a > b:
    if a > c:
        ret = a
    else:
        ret = c
else:
    if b > c:
        ret = b
    else:
        ret = c
print "El mayor de los numeros es: %s" % ret
