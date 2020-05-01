b=str(input("introduce la palabra para quitarle las vocales:  "))

vocales = ('a', 'e', 'i', 'o', 'u')

for letra in vocales:
    b = b.replace(letra, "")
print(b)
