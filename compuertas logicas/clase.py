import random
poblacion=[8, 4, 7, 1, 7, 6]
print("generacion 0", poblacion)
print("poblacion inicial:", poblacion)
padres = poblacion[:3]
print("padres seleccionados:", padres)

hijos = []
for i in range (0, len(padres) -1):
    for j in range (i + 1, len(padres)):
        padre1 = padres [i]
        padre2 = padres [j]
        hijo1 = padre1 + padre2
        hijo2 = padre1 * padre2
        hijos.append(hijo1)
        hijos.append(hijo2)


mutado = random.randint(0, len(hijos)-1)
hijos[mutado] = int(str(hijos[mutado])[::-1])

print("generacion 1- hijos despues de la mutacion", hijos)

individuos = hijos
maximo  = max(individuos)
print("numero natural mas grande encontrado", maximo)

generacion = 1
while maximo <= 1000:
    padres = individuos[:3]
    hijos = []
    for i in range (0, len(padres) -1):
        for j in range (i + 1, len(padres)):
            padre1 = padres [i]
            padre2 = padres [j]
            hijo1 = padre1 + padre2
            hijo2 = padre1 * padre2
            hijos.append(hijo1)
            hijos.append(hijo2)
    
    mutado = random.randint(0, len(hijos)-1)
    hijos[mutado] = int(str(hijos[mutado])[::-1])
    print(f"generacion{generacion}-hijos despues de la mutacion", hijos)
    individuos = hijos
    print(f"generacion{generacion}-poblacion final", individuos)
    maximo  = max(individuos)
    print("numero natural mas grande encontrado", maximo)
    