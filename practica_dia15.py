# practica_dia15.py - dia 15: cierre de racha - limpieza final + reporte

def leer_progreso(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip() != ""]

def  limpiar_linea(linea):
    if ":" in linea:
        izq, der = linea.split(":", 1)
        # con f - esta es la que te falto antes

        return f"{izq.strip()}: {der.strip()}"
    return linea.strip()
def guardar(ruta, lineas):
    with open(ruta, "w", encoding="utf-8") as f:
        for linea in lineas:
            f.write(linea + "\n")

# --- main ---
print(" === dia 15 - cierre final ===")
lineas = leer_progreso("progreso.txt")
print(f"antes: {len(lineas)} lineas")

#1. limpiar todas
limpias = [limpiar_linea(linea) for linea in lineas]
# 2. duplicar manteniendo orden - deja solo 1 dia 10
vistos = set()
final = []
for linea in limpias:
    # clave = numero de dia
    parte = linea.lower().split()
    if len(parte) >= 2 and parte[0] == "dia":
        num = parte[1].replace(":", "")
        if num in vistos:
            # si ya vimos dia 10 lo saltamos
            print(f"duplicadp eliminado:[linea]")
            continue
        vistos.add(num)
    final.append(linea)

print(f"despues: {len(final)} lineas unicas")
print(f"dias: {sorted(vistos, key=lambda x: int (x))}")

#3. guardar progreso limpio
guardar("progreso.txt", final)

# 4. generar analisis.txt final para portafolio
conteo = {}
palabras = []
for linea in final:
    for p in linea.split():
        limpia = p.replace(":", "").lower()
        palabras.append(limpia)
        conteo[limpia] = conteo.get(limpia, 0) + 1

mas_repetida = max(conteo, key=conteo.get)

with open("analisis.txt", "w", encoding="utf-8") as f:
    f.write(f"reporte final my return 2026 - 15 dias\n")
    f.write(f"total lineas: {len(final)}\n")
    f.write(f"total palabras: {len(palabras)}\n")
    f.write(f"palabra mas repetida: {mas_repetida} ({conteo[mas_repetida]} veces)\n")
    f.write(f"dias completados: {sorted(vistos, key=lambda x: int(x))}\n")
    f.write(f"racha: {len(final)} dias imparable desde chaclacayo\n")

print("progreso.txt limpio guardado")
print("analisis.txt generado")
print("abre analisis.txt y veras tu certificado")




