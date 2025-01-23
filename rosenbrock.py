# First session


def hc_min():
  pass


def random_min(func, xlow, xhigh, n):
  xmin = 0
  return xmin
  
# 𝑓(𝑥) = 100(𝑥2 − 𝑥1^2)^2 + (1 − 𝑥1)^2
def rosenbrock(x):
  return 100 * (x[1] - x[0]**2)** 2 + (1 - x[0])**2


if __name__ == '__main__':
  xlow = (-5, -5)
  xhigh = (5, 5)
  xmin = random_min(rosenbrock, xlow, xhigh, 100)
  print(xmin)
  
  x = (1, 2)
  f = rosenbrock(x)
  print(f)
  
  