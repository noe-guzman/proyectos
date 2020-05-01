import math
print ("ingrese una seria de 10 numeros")
a = float (input())
b = float (input())
c = float (input())
d = float (input())
e = float (input())
f = float (input())
g = float (input())
h = float (input())
i = float (input())
j = float (input())
me = float (a+b+c+d+e+f+g+h+i+j)
print("la media de los numeros ingresados es: " ,me)

#desviacion estandar

da = float (a-me)
db = float (b-me)
dc = float (c-me)
dd = float (d-me)
de = float (e-me)
df = float (f-me)
dg = float (g-me)
dh = float (h-me)
di = float (i-me)
dj = float (j-me)

#se elevaron al cuadrado
DA = float  (da**2)
DB = float  (db**2)
DC = float  (dc**2)
DD = float  (dd**2)
DE = float  (de**2)
DF = float  (df**2)
DG = float  (dg**2)
DH = float  (dh**2)
DI = float  (di**2)
DJ = float  (dj**2)

#suma de los numeros elavados al cuadrado aplicando la division de N-1

ds = (DA + DB + DC + DD + DE + DF + DG + DH + DI + DJ)/(10-1)

#raiz cuadrada del total de la suma 
dt = math.sqrt(ds)

print ("la desviacion estandar es: ", dt)

#moda 
from statistics import mode
x = [a, b, c, d, e, f, g ,h , i, j]
print("la moda es: " ,mode(x))

