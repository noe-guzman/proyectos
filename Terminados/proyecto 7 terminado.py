b = str(input("ingrese el nombre con el que quiere guardar el archivo con la teminacion .txt donde quiere guardar su palabra"))

archi1=open(b,"w") 

a= str(input("ingrese una para guardar: "))
archi1.write(a) 
print("\n" )
archi1.write("batman\n") 
archi1.write("ya me desespere de hacer tareas\n")  
archi1.close() 