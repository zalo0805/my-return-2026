print("--- practica 1- inico y ahora---")

#1. abre tu historia
with open("progreso.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# 2. cuantas lineas tienes?
racha = len(lineas)
print(f"tienes {racha} lineas en total")

#3. la magia de las listas
primera = lineas[0].strip() # [0] es siempre el primero
ultima = lineas[-1].strip() # [-1] es siempre el ultimo, no importa cuantos tengas

print(f"\n tu dia 1 fue {primera}")
print(f" tu dia {racha} es {ultima}")

#4. un if para ti
if primera == ultima:
    print("ojo, repetiste lo mismo que el dia 1")
else:
    print(f"mira cuanto avanzaste desde {primera} hasta {ultima}")



#nivel 1.5 - cuanto te falta para 15?
meta = 15
faltan = meta - racha

print(f"\n --- meta doble digito fuerte: {meta}---")
if faltan <= 0:
    print(f" ya pasaste los {meta} eres imparable")
else:
    print(f"te faltan {faltan} dias para llegar a{meta}")
    print(f"si sigues asi, llegas en {faltan} dias")

# nivel 2 - cuantas veces dijiste "dev"?
contador_dev = 0
for linea in lineas:
    if "dev" in linea.lower():
        contador_dev = contador_dev + 1

print(f"\n --- analisis de tu historia---")
print(f"has escrito 'dev' {contador_dev} veces")
