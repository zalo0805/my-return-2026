print("--- dia 8 - guardando mi progreso ---")

def guardar_progreso(texto):
    archivo = open("progreso.txt", "a", encoding="utf-8")
    archivo.write(texto + "\n")
    archivo.close()
    print("-> guardado en progreso.txt")

def mostrar_progreso():
    print("\n --- MI HISTORIAL COMPLETO ---")
    try:
        archivo = open("progreso.txt", "r", encoding="utf-8")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except:
        print(" aun no hay historial, hoy es el primer guardado")

#programa principal
hoy = input("que aprendiste hoy?")
guardar_progreso(f"dia 8: {hoy}")
ver = input("quieres ver todo tu historial? (s/n):")
if ver == "s":
    mostrar_progreso()

print("\n¡dia 8 copmpletado! ya guardas datos como un dev real")

