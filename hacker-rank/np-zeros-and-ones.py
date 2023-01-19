import numpy

x = tuple(map(int, input().split()))
print(numpy.zeros(x, dtype=int))
print(numpy.ones(x, dtype=int))