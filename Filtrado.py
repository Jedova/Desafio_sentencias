##Actividad 1 - Filtrado compacto

ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

umbral = int(input("ingresa un valor límite: "))
respuesta ={}

for i, v in ventas.items():
    if v>umbral:
     respuesta[i] = v
print ("Los meses que superan el umbral definido son:")
print (respuesta)
