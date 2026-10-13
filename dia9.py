print("-- dia 9 - mi contador de racha ---")
def contar_dias():
    try:
        archivo = open("progreso.txt", "r", encoding ="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        return len(lineas)
    except:
        return 0

racha = contar_dias()
print(f"Llevas {racha} dias seguidos, gonzalo!")
print(f"semana 1: 7/7, semana 2: {racha -7}/7")

if racha >= 8:
    print("¡semana 2 imparable! lima no para")

# hoy tambien guardamos
hoy = input("que lograste hoy? ")
archivo = open("progreso.txt", "a", encoding="utf-8")
archivo.write(f"dia 9: {hoy}\n")
archivo.close()

print(" dia 9 guardado!")

