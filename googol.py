import random

objetivo = 10**100
poblacion=[8, 4, 7, 1, 7, 6]

print("generacion 0", poblacion)
print("poblacion inicial:", poblacion)

mejor = 0

padres = poblacion[:3]
print("padres seleccionados:", padres)

hijos = []
for i in range (0, len(padres) -1):
    for j in range (i + 1, len(padres)):
        padre1 = padres[i]
        padre2 = padres[j]

        hijo1 = padre1 + padre2
        hijo2 = padre1 * padre2
        hijo3 = padre1 ** 2
        hijo4 = padre2 ** 2

        hijos.extend([hijo1, hijo2, hijo3, hijo4])

# mutación
mutado = random.randint(0, len(hijos)-1)
hijos[mutado] = int(str(hijos[mutado])[::-1])

print("generacion 1- hijos despues de la mutacion", hijos)

individuos = hijos
generacion = 1
maximo = max(individuos)

while maximo <= objetivo:
    nuevos = []

    # FILTRO + MEJOR
    for num in individuos:
        if num <= objetivo:
            nuevos.append(num)
            if num > mejor:
                mejor = num

    if not nuevos:
        break

    # ORDENAR POR CERCANÍA
    nuevos.sort(key=lambda x: objetivo - x)

    print(f"generacion{generacion}-mejor hasta ahora", nuevos[0])

    # SELECCIÓN INTELIGENTE
    padres = nuevos[:3]

    hijos = []

    for i in range (0, len(padres) -1):
        for j in range (i + 1, len(padres)):
            padre1 = padres[i]
            padre2 = padres[j]

            hijo1 = padre1 + padre2
            hijo2 = padre1 * padre2
            hijo3 = padre1 ** 2
            hijo4 = padre2 ** 2

            hijos.extend([hijo1, hijo2, hijo3, hijo4])

    # mutación
    if random.random() < 0.3:
        mutado = random.randint(0, len(hijos)-1)
        hijos[mutado] = int(str(hijos[mutado])[::-1])
    print(f"\n {'-'*54}")
    print(f"\n generacion{generacion}-hijos despues de la mutacion", hijos)
    print(f"\n {'-'*54}")
    # SOLO LOS MEJORES SOBREVIVEN
    individuos = sorted(hijos, key=lambda x: objetivo - x if x <= objetivo else float('inf'))[:6]

    print(f"generacion{generacion}-poblacion final", individuos)

    generacion += 1

print("\n numero mas cercano al googol sin pasarse:")
print(mejor)
