# practica_dia14.py  - dia 14: limpieza de datos

def leer_progreso(ruta):
    with open(ruta, "r", encoding = "utf-8") as f:
        lineas = f.readlines()
    return [l.strip() for l in lineas if l.strip()!=""]

def limpiar_linea(linea):
    # arregla "dia 10 :mejorar" -> "dia 10: mejorar"
    # y "dia 8: dia 8" -> "dia 8: dia 8" ya esta bien

    if ":" in linea:
        partes = linea.split(":", 1)
        izquierda = partes[0].strip()
        derecha = partes[1].strip()
        return f"{izquierda}: {derecha}"
    return linea.strip()

def guardar_progreso(ruta, lineas_limpias):
    with open(ruta, "w", encoding="utf-8") as f:
        for l in lineas_limpias:
            f.write(l + "\n")

# ---- programa principal----
print("===limpieza dia 14===")
lineas = leer_progreso("progreso.txt")
print(f"lineas leidas:{len(lineas)}")

lineas_limpias = []
dias_vistos = set()
for l in lineas:
    limpia = limpiar_linea(l)
    lineas_limpias.append(limpia)
    #sacar numero de dia
    if limpia.startswith("dia"):
        try:
            num = limpia.split()[1].replace(":", "")
            dias_vistos.add(num)
        except:
            pass

print(f"dias unicos encontrados: {len(dias_vistos)} ->{sorted(dias_vistos)}")

#guardar limpio
guardar_progreso("progreso.txt", lineas_limpias)
print("progreso.txt limpiado y guardado")
print("revisa tu progreso.txt, ahora todo tiene ': ' con espacio")
