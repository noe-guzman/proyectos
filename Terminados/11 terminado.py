numeros = []
while True:
    pedirNumero = float(input("Ingresa un numero mayor a 1 y menor a 10, para parar ingrese 0: "))
    if pedirNumero == 0:
        break
    else:
        if pedirNumero > 1.0 and pedirNumero < 11.0:
            numeros.append(pedirNumero)
        else:
            print("Numero invalido :(")
numeros = sorted(numeros, reverse = True)
print(numeros)
if int(numeros[0]) == 1:
    print("Uno")
if int(numeros[0]) == 2:
    print("Dos")
if int(numeros[0]) == 3:
    print("Tres")
if int(numeros[0]) == 4:
    print("Cuatro")
if int(numeros[0]) == 5:
    print("Cinco")
if int(numeros[0]) == 6:
    print("Seis")
if int(numeros[0]) == 7:
    print("Siete")
if int(numeros[0]) == 8:
    print("Ocho")
if int(numeros[0]) == 9:
    print("Nueve")
if int(numeros[0]) == 10:
    print("diez")