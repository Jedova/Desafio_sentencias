#### Simulación de primeros auxilios##

respuesta = input("¿La persona responde a estimulos? (si/no): ").lower()

while respuesta not in ("no", "si"):
    respuesta = input("la respuesta debe ser si o no: ").lower()
if respuesta =="si":
    print("Valora la necesidad de llevarlo/a al hospital más cercano")
else:    
    print("Abrir las vías aérea")
  
    respuesta2 = input("¿Respira? (si/no): ").lower()

    while respuesta2 not in ("no", "si"):
        respuesta2 = input("la respuesta debe ser si o no: ").lower()
    if respuesta2 =="si":
        print("Ubiquelo/a en una posición que le brinde suficiente ventilación")
    else:    
        print("Administrar 5 ventilaciones y llamar a la ambulancia")

        respuesta3 = input("¿Signos de vida? (si/no): ").lower()

        while respuesta3 not in ("no", "si"):
            respuesta3 = input("la respuesta debe ser si o no: ").lower()
        if respuesta3 =="si":
            print("Re-evaluar a la espera de la ambulancia")
        else:    
            print("Administrar compresiones torácicas hasta que llegue la ambulancia")

            respuesta4 = input("¿Llegó la ambulancia? (si/no): ").lower()

            while respuesta4 not in ("no", "si"):
                respuesta4 = input("la respuesta debe ser si o no: ").lower()
            
            while respuesta4 == "no":
                respuesta3 = input("¿Signos de vida? (si/no): ").lower()
                
                while respuesta3 not in ("no", "si"):
                    respuesta3 = input("la respuesta debe ser si o no: ").lower()
                if respuesta3 =="si":
                    print("Re-evaluar a la espera de la ambulancia")
                else:    
                    print("Administrar compresiones torácicas hasta que llegue la ambulancia")       
                respuesta4 = input("¿Llegó la ambulancia? (si/no): ").lower()
    
                while respuesta4 not in ("no", "si"):
                    respuesta4 = input("La respuesta debe ser si o no: ").lower()
print("Fin")