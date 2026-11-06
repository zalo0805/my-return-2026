# agregar_dia.py  -dia 17: automatizando mi racha
from datetime import datetime

frase = input("que hiciste hoy? ej dia 17: mi primer script automatico \n> ")
fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
with open("analisis.txt", "a", encoding="utf-8") as f:
     f.write(f"\n{frase} - {fecha}")

print(f"\n✅ agregado: {frase}")
print("ahora haz tu git push para guardar la racha")
