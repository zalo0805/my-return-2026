print(" --- caluculadora de retorno ---")
anios_texto = input("cuantos anios sin programar?")
anios = int(anios_texto)
meses = anios * 12
dias = anios * 365
horas = dias * 24
print(f"wow, {anios} anios son:")
print(f" - {meses} meses")
print(f" - {dias} dias")
print(f" - {horas} horas lejos del codigo")

if anios >= 10:
    print("10 anios es un monton, pero volviste, eres de los fuertes!")
else:
    print("volviste rapido, aun lo mtienes fresco!")
