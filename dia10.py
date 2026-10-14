print(" ---- dia 10 - doble digito ---")

archivo = open("progreso.txt", "r", encoding="utf-8")
lineas = archivo.readlines()
archivo.close()

racha = len(lineas)
print(f"llevas {racha} dias, gonzalo!")

if racha <10:
    print("a un paso del doble digito")
elif racha == 10:
    print("¡¡10 dias!! ya no hay vuelta atras eres dev")
else:
    print("doble digito imparable, lima no para")

hoy = input("que te hizo quedarte hoy?")
archivo = open("progreso.txt", "a", encoding="utf-8")
archivo.write(f"dia 10:{hoy}\n")
archivo.close()
