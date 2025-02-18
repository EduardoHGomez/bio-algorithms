# First session: Make the following functions with hill climbing algorithm
import random
import math

# Rosenbrock
# Rastrigin
# Styblinsky-Tang

def hc_min(min_start, xlow, xhigh):
    pass

# 𝑓(𝑥) = 100(𝑥2 − 𝑥1^2)^2 + (1 − 𝑥1)^2
def rosenbrock(x): # Receiving an array
	# x[0] = x1
	# x[1] = x2
	return 100 * (x[1] - x[0]**2)** 2 + (1 - x[0])**2

# Rastrigin
def rastrigin(x):
    return 20 + (x[0]**2 - 20 * math.cos(2 * math.pi * x[0])) + (x[1]**2 - 20 * math.cos(2 * math.pi * x[1]))

# Styblinski-Tang
def styblinski_tang(x):
    return 0.5 * ((x[0]**4 - 16 * x[0]**2 + 5 * x[0]) + (x[1]**4 - 16 * x[1]**2 + 5 * x[1]))


def random_min(func, xlow, xhigh, n):
    # Seleccionar el random minimo con n iteraciones
    least_x = None  # Almacenar el minimo x arreglo
    least_value = float('inf')  # Inicia con infinito pues es como el valor maximo

    for i in range(n):
        x1 = random.uniform(xlow[0], xhigh[0])
        x2 = random.uniform(xlow[1], xhigh[1])
        x = [x1, x2]
        value = func(x)
        if value < least_value:
            least_x = x
            least_value = value

    return least_x


if __name__ == '__main__':
    xlow = (-5, -5)
    xhigh = (5, 5)

    n = 100
    for i in range(3):
        print(f"Rosenbrockr con {n} iteraciones", "x*:", random_min(rosenbrock, xlow, xhigh, n), "f(x*):", rosenbrock(random_min(rosenbrock, xlow, xhigh, n)))
        print(f"Rastrigin con {n} iteraciones", "x*:", random_min(rastrigin, xlow, xhigh, n), "f(x*):", rastrigin(random_min(rastrigin, xlow, xhigh, n)))
        print(f"Styblinski-Tang con {n} iteraciones", "x*:", random_min(styblinski_tang, xlow, xhigh, n), "f(x*):", styblinski_tang(random_min(styblinski_tang, xlow, xhigh, n)))
        print('------------------')

        n *= 100