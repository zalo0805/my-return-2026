# practica_dia13.py - dai 13 funciones

def leer_progreso(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read().lower().split()

def contar_palabras(palabras):
    conteo = {}
    for p in palabras:
        limpia = p.replace(":", "").strip()
        if limpia == "":
            continue
        conteo[limpia] = conteo.get(limpia, 0) + 1
    return conteo

def palabra_ganadora(conteo):
    mas_repetida = ""
    max_veces = 0
    for palabra, cantidad in conteo.items():
        if cantidad > max_veces:
            max_veces = cantidad
            mas_repetida = palabra
    return mas_repetida, max_veces

#--- programa principal---
palabras = leer_progreso("progreso.txt")
conteo = contar_palabras(palabras)
ganadora, veces = palabra_ganadora(conteo)

print(f"total palabras: {len(palabras)}")
print(f"ganadora: '{ganadora}' con {veces} veces")
print("dia 13 con funciones")
