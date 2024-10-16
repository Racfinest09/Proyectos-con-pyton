redes = []
conter = 1
while conter!=0:
    conter =int(input("¿Va a ingresar una nueva red? oprima 1 para si o 0 para no: "))
    if conter==0:
      break
    id=input("Ingrese el nombre de la red wifi: ")
    contraseña=input("Ingrese la contraseña: ")
    redes.append(id)
    redes.append(contraseña)
print(redes)