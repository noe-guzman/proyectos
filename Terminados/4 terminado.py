a = str(input ("ingrese la palabra para contar sus consonantes"))
b =list(a)
c = [ 'b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B','C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
contador = 0
for i in b:
  for x in c:
    if i == x:
      contador = contador + 1
print("Consonantes: ", contador)


