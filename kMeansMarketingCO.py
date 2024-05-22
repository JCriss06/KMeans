import random
import numpy
def maximMinim(dsT):
    maxim = []
    minim = []
    for i in dsT:
        maxim.append(int(max(i)))
        minim.append(int(min(i)))
    return maxim, minim

def ActualizaCent(dataset, grupos, cent):
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            cent[i][j] = 0
        cont[i] = 0
    for i in range(len(grupos)):
        for j in range(len(dataset[i])):
            cent[grupos[i]][j] += dataset[i][j]
        cont[grupos[i]] += 1
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            if cont[i] != 0:
                cent[i][j] /= cont[i]

def CalcDist(point, centroide):
    total = 0
    for i in range(m):
        total += (point[i] - centroide[i])**2
    return total

def CalculaGrupos(dataset, cent, grupos):
    continuar = False
    for ip in range(n):
        distMin = float("+inf")
        indexMin = float("+inf")
        for ic in range(k):
            dist = CalcDist(dataset[ip], cent[ic])
            if dist < distMin:
                distMin = dist
                indexMin = ic
        if grupos[ip] != indexMin:
            continuar = True
            grupos[ip] = indexMin
    return continuar

#Graph no es necesario

if __name__ == "__main__":
    file = open("MarketingCampaingOut.csv", "r")
    k = 9
    dataset = []
    for linea in file:
        elem = linea.strip().split(",")
        dataset.append(elem)
    cabecera = dataset.pop(0)
    # n es el numero de renglones
    n = len(dataset)
    # m es el numero de columnas
    m = len(cabecera)
    for i in range(n):
        for j in range(m):
            dataset[i][j] = float(dataset[i][j])
    dsT = list(zip(*dataset))
    cent = [[0 for i in range(m)] for j in range(k)]

    maxim, minim = maximMinim(dsT)
    for i in range(k):
        for j in range(m):
            cent[i][j] = random.randint(minim[j], maxim[j])
    grupos = [0 for i in range(n)]
    cont = [0 for i in range(k)] # ver

    continuar = True
    while continuar:
        continuar = CalculaGrupos(dataset, cent, grupos)
        ActualizaCent(dataset, grupos, cent)

    cont = [0 for i in range(k)]
    prom = [0 for i in range(k)]
    for i in range(n):
        prom[grupos[i]] += CalcDist(dataset[i], cent[grupos[i]])
        cont[grupos[i]] += 1

    for i in range(k):
        if cont[i] != 0:
            prom[i] = prom[i] / cont[i]
    promDistGlobal = numpy.average(prom)

    print("Promedio Distancia Global =", promDistGlobal)