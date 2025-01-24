# First session: Make the following functions with hill climbing algorithm

# Rosenbrock
# Rastrigin
# Styblinsky-Tang

  
# 𝑓(𝑥) = 100(𝑥2 − 𝑥1^2)^2 + (1 − 𝑥1)^2
def rosenbrock(x): # Receiving an array
	# x[0] = x1
	# x[1] = x2
	return 100 * (x[1] - x[0]**2)** 2 + (1 - x[0])**2


# Hill Climbing algorithm


def random_min(func, xlow, xhigh, n):
	# Minimun randomn
	xrand1 = random.randint(xlow[0], xhigh[0])
	xrand2 = random.randint(xlow[1], xhigh[1])

	# Evaluate the solution


	return xmin


if __name__ == '__main__':
	xlow = (-5, -5)
	xhigh = (5, 5)
	xmin = random_min(rosenbrock, xlow, xhigh, 100)
	print(xmin)
	