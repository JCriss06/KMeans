import random

padre1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
padre2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def crossover_one_point(parent1, parent2):
    # Seleccionar un punto de cruce aleatorio
    punto_cruce = random.randint(1, len(parent1) - 1)

    # Realizar el cruce de un punto
    hijo1 = parent1[:punto_cruce] + parent2[punto_cruce:]
    hijo2 = parent2[:punto_cruce] + parent1[punto_cruce:]

    return hijo1, hijo2

# Ejemplo de cruzamiento
descendiente1, descendiente2 = crossover_one_point(padre1, padre2)

# Imprimir resultados
print("Padre 1:", padre1)
print("Padre 2:", padre2)
print("Descendiente 1 después del cruce:", descendiente1)
print("Descendiente 2 después del cruce:", descendiente2)
