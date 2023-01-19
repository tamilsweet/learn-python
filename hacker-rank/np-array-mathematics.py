import numpy

N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor_divide(A, B))
print(numpy.mod(A, B))
print(numpy.power(A, B))