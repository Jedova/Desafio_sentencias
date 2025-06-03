##Fuerza bruta##
from string import ascii_lowercase as a ## entrega un abecedario en minuscula
from getpass import getpass # permite cubrir el pass

Contraseña = getpass("Ingrese la contraseña: ").lower() ## se busca que todo lo ingresado sea minuscula
n=0
e=""

for i in Contraseña:
    for ii in a:
        n+=1
        if ii == i:
            e +=ii
            break

print(f"Contraseña encontrada: {e}")
print(f"Total de intentos realizados: {n}")

    
