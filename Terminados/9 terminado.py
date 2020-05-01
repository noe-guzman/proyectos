a = []
cantidad = 10
i = 1

while (cantidad > 0):
    b = int(input("ingrese los numeros a ordenar # " + str(i) + ": "))
    a.append (b)
    i= i + 1
    cantidad = cantidad - 1

def comparer (c):
    return -c

a.sort(key=comparer)
print (a)



