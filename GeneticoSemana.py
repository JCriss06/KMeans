import math
import random as rand
import numpy as np
import os

if __name__ == "__main__":
    archivos = os.listdir("TSP Instances")
    for archivo in archivos:
        # region inicializa variables
        n = 10
        pop_size = 200
        p = [[i for i in range(n)] for j in range(int(pop_size/2))]
        vo = [0 for i in range(pop_size)]
        vivos = [False for i in range(pop_size)]
        #endregion
        #region Lectura de instancia
        file = open("TSP Instances/{0}".format(archivo),"r")
        file.readline()
        file.readline()
        file.readline()
        n = int(file.readline().strip().split(":")[1])
        file.readline()
        file.readline()
        cities = np.zeros((n,2))
        for i in range(n):
            cities[i] = file.readline().strip().split(" ")[1:]
        graph = np.zeros((n,n))
        for i in range(n-1):
            for j in range(i+1,n):
                graph[i][j] = int(math.sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2))
                graph[j][i] = graph[i][j]
        n = 10
        #endregion
        #region Inicializa P
        for i in range(len(p)):
            vivos[i] = True
            for j in range(n-1):
                it = rand.randint(j, n-1)
                temp = p[i][it]
                p[i][it] = p[i][j]
                p[i][j] = temp

        p.extend([[0 for i in range(n)] for j in range(int(pop_size/2))])
        #endregion
        itersSinMejora = 10
        BestGlobal = float("+Inf")
        limiteMuerte = int(pop_size * .75)
        while itersSinMejora > 0:
            itersSinMejora -= 1
            #region Cruza y Muta(no muta por lo pronto)
            for i in range(pop_size):
                if vivos[i] == False:
                    p1 = rand.randint(0, pop_size - 1) # generamos el padre 1
                    while(vivos[p1] == False):
                        p1 = rand.randint(0, pop_size - 1) # si el padre 1 esta muerto, generamos otro padre 1

                    p2 = rand.randint(0, pop_size - 1) # gereramos el padre 2
                    while (vivos[p2] == False or p2 == p1):
                        p2 = rand.randint(0, pop_size - 1) # verificamos que le padre 2 no sea igual que el padre 1 o que este no este muerto, sino generamos otro
                    j1 = rand.randint(0,n)
                    j2 = rand.randint(0,n)
                    if j2 < j1:
                        temp = j2
                        j2 = j1
                        j1 = temp
                    seleccionados = [0 for i in range(n)]
                    for j in range(n):
                        p[i][j] = -1
                    for j in range(j1,j2):
                        p[i][j] = p[p1][j]
                        seleccionados[p[p1][j]] = 1
                    j2 = 0
                    for j1 in range(n):
                        while j2 < n and p[i][j2] != -1:
                            j2 += 1
                        if seleccionados[p[p2][j1]] == 0:
                            p[i][j2] = p[p2][j1]
                            j2 += 1
            for i in range(pop_size):
                vivos[i] = True
            #endregion
            #region Evaluacion y Seleccion Elitista
            for i in range(pop_size):
                vo[i] = 0
                for j in range(n-1):
                    vo[i] += graph[p[i][j]][p[i][j+1]]
                vo[i] += graph[p[i][-1]][p[i][0]]
            minActual = min(vo)
            if minActual < BestGlobal:
                BestGlobal = minActual
                itersSinMejora = 10
            prom = np.average(vo)
            muertos = 0
            for i in range(pop_size):
                if vo[i] > prom:
                    vivos[i] = False
                    muertos += 1
                    if muertos >= limiteMuerte:
                        break
            # endregion

        BestGlobal = min(vo)
        print("Archivo = {0} BestGlobal = {1}".format(archivo, BestGlobal))
        # for e in enumerate(zip(p,vo,vivos)):
        #     print(e)
