# practica_dia12.py - dia 12: tu palabra mas usada

with open("progreso.txt", "r", encoding = "utf-8") as archivo:
    texto = archivo.read().lower()
    palabras = texto.split()

conteo = {}

for palabra in palabras:
    # limpiamos dos puntos y espacios
    palabra_limpia = palabra.replace(":", "").strip()
    if palabra_limpia =="":
        continue
    if palabra_limpia in conteo:
        conteo[palabra_limpia] = conteo[palabra_limpia] + 1
    else:
        conteo[palabra_limpia] = 1

print("--- conteo de palabras")
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad} veces")

# buscamos la ganadora
mas_repetida = ""
max_veces = 0
for palabra, cantidad in conteo.items():
    if cantidad > max_veces:
        max_veces = cantidad
        mas_repetida = palabra
print(f"\n tu palabra mas repétida es '{mas_repetida}' con {max_veces} veces")
print(f" ¡has escrito '{mas_repetida}' {max_veces} dias seguidos sin fallar!")
