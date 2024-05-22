import random

import matplotlib.pyplot as plt
def maximMinim(dsT):
    maxim = []
    minim = []
    for i in dsT:
        maxim.append(int(max(i)))
        minim.append(int(min(i)))
    return maxim, minim

def ActualizaCent (dataset, grupos, cent):
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
            cent[i][j] /= cont[i]

def CalcDist(point, centroide):
    total = 0
    for i in range(len(point)):
        total += (point[i] - centroide[i])**2
    return total

def CalculaGrupos(dataset, cent, grupos):
    continuar = False
    for ip in range(len(dataset)):
        distMin = float("+inf")
        indexMin = float("+inf")
        for ic in range(len(cent)):
            dist = CalcDist(dataset[ip], cent[ic])
            if dist < distMin:
                distMin = dist
                indexMin = ic
        if grupos[ip] != indexMin:
            continuar = True #-
            grupos[ip] = indexMin
    return continuar

def Graph(dsT, grupos, centroides = None):
    colors = dict()
    grupColor = [e * 50 for e in grupos]
    fig, ax = plt.subplots()
    ax.scatter(dsT[0], dsT[1], c=grupColor)
    CT = list(zip(*centroides))
    ax.scatter(CT[0], CT[1], color="red")
    plt.show()
    plt.close()

if __name__ == "__main__":
    file = open("2d For Clustering/pathbased.txt", "r")
    k = 3
    dataset = []
    originalG = []
    for line in file:
        elem = line.strip().split("\t")
        for i in range(len(elem)):
            elem[i] = float(elem[i])
        originalG.append(int(elem.pop(2)))
        dataset.append(elem)
    dsT = list(zip(*dataset))
    cent = [[0 for i in range(len(dsT))] for j in range(k)]

    maxim, minim = maximMinim(dsT)
    for i in range(k):
        for j in range(len(dsT)):
            cent[i][j] = random.randint(minim[j], maxim[j])
    grupos = [0 for i in dataset]
    cont = [0 for i in range(k)]

    continuar = True
    while continuar:
        continuar = CalculaGrupos(dataset, cent, grupos)
        Graph(dsT, grupos, cent)
        ActualizaCent(dataset, grupos, cent)
        Graph(dsT, grupos, cent)

    for e in cent:
        print(e)