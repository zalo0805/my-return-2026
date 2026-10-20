# practica_dia16.py - dia 16: mi readme para github

def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

print(" ==== dia 16 - generando readme ===")

# 1. leemos lo que ya lograste
progreso_texto = leer_archivo("progreso.txt")
analisis_texto = leer_archivo("analisis.txt")

# 2. creamos el readme bonito
with open("readme.md", "w", encoding="utf-8") as f:
    f.write(" #my return 2026 - 15 dias imparable desde lima\n\n")
    f.write(" este es mi regreso a la programacion. 15 dias seguidos codificando sin fallar \n\n")
    f.write("## racha actual\n\n")
    f.write("''\n")
    f.write(analisis_texto)
    f.write("\n'''\n\n")
    f.write("## mi progreso diario\n\n")
    f.write("'''\n")
    f.write(progreso_texto)
    f.write("\n'''\n\n")
    f.write("## tecnologias\n")
    f.write(" - python - limpieza de datos, sets, dicts\n")
    f.write(" -git & github - 15 commits seguidos\n")
    f.write(" - manejo de archivos .txt\n\n")
    f.write("hecho con disciplina desde lima, racha imparable. \n")

print("readme.md generado!")
print(" ahora abre readme.md y dime que ves")
