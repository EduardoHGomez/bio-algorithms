import random
from random import randrange
from random import uniform


def random_net(n):
    return [[int(uniform(1, 2 * n)) for _ in range(n)] for _ in range(n)]


net1 = [[0, 4, 2, 1], [3, 0, 6, 5], [2, 3, 0, 2], [3, 8, 2, 0]]   # min_distance = 9
net2 = [[0, 4, 2, 1, 3, 5, 5, 6, 8, 6], [3, 0, 6, 5, 7, 2, 2, 5, 8, 2], [2, 3, 0, 2, 1, 4, 6, 8, 5, 4],
        [3, 8, 2, 0, 4, 5, 7, 9, 6, 5], [6, 1, 3, 8, 0, 2, 4, 7, 9, 1], [1, 2, 3, 4, 5, 0, 5, 9, 7, 8],
        [1, 2, 3, 4, 5, 6, 0, 4, 8, 3], [6, 5, 4, 3, 2, 1, 7, 0, 5, 3], [6, 3, 8, 7, 9, 1, 2, 5, 0, 5],
        [7, 3, 8, 9, 1, 2, 6, 5, 4, 0]]  # min_distance = 19
net3 = random_net(11)  # min_distance = ??
net  = net3


#### Algoritmo exhaustivo
def process(st, k, visited, solution, d):
    n = len(net)
    last = solution[k - 1]
    if k == n:
        d += net[last][st]
        return d

    res = float('inf')
    for i in range(n):
        if not visited[i]:
            visited1 = list(visited)
            solution1 = list(solution)
            visited1[i] = True
            solution1[k] = i
            res = min(res, process(st, k + 1, visited1, solution1, d + net[last][i]))
    return res


def tsp_exhaustive(st):
    n = len(net)
    visited = [True if i == st else False for i in range(n)]
    solution = [st if i == 0 or i == n else -1 for i in range(n + 1)]
    return process(st, 1, visited, solution, 0)


#### Algoritmo vecino más cercano
def get_nearest(st, visited):
    min_distance = float('inf')
    res = -1
    for i in range(len(net)):
        d = net[st][i]
        if d < min_distance and i not in visited:
            res = i
            min_distance = d
    return res


def tsp_nearest_neighbor(start):
    min_distance = 0
    current = start
    visited = {start}
    for i in range(len(net) - 1):
        nearest = get_nearest(current, visited)
        visited.add(nearest)
        min_distance += net[current][nearest]
        current = nearest
    min_distance += net[current][start]
    return min_distance


#### Algoritmo aleatorio
def eval(start, solution):
    d = 0
    current = start
    for i in range(len(solution)):
        next = solution[i]
        d += net[current][next]
        current = next
    d += net[current][start]
    return d


def tsp_random(start, n):
    l = len(net) - 1
    solution = [i if i != start else l for i in range(l)]
    minD = eval(start, solution)
    for i in range(n):
        random.shuffle(solution)
        d = eval(start, solution)
        if d < minD:
            minD = d
    return minD


# Recocido simulado (simulated annealing)
def swap(solution):
    # rand between 0 and len(solution)
    i = randrange(0, len(solution))
    j = randrange(0, len(solution))

    solution[i], solution[j] = solution[j], solution[i]
    return solution


def inverse(solution):
    i = randrange(0, len(solution))
    j = randrange(0, len(solution))
    # Reverse the subsequence between i and j
    if i > j:
        i, j = j, i
    
    for i in range(i, j):
        solution[i], solution[j] = solution[j], solution[i]

    return solution

def move_to_neighbor(solution):
    pass


# funcion fitness (energía)
def f(start, solution):
    return 1 / eval(start, solution)


def tsp_sa(start, n):
    T = 100
    alpha = 0.99
    d = 100000  # distancia mínima
    # x1 = permutación aleatoria sin incluir start
    for i in range(n):
        # x2 = un nuevo vecino de x1
        # calcular fx1, fx2
        # si x2 mejoró/empató a x1, reemplazarlo
        # si no, utilizar la distribución de probabilidad de Boltzmann
        # actualizar d
        pass
    return d


if __name__ == '__main__':
    minD = tsp_random(0, 1000)
    print(minD)
    minD = tsp_nearest_neighbor(0)
    print(minD)
    minD = tsp_exhaustive(0)
    print(minD)
