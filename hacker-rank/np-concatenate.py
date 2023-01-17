import numpy

N, M, P = map(int, input().split())
arr1 = numpy.array([list(map(int, input().split())) for i in range(N)])
arr2 = numpy.array([list(map(int, input().split())) for i in range(M)])
print(numpy.concatenate((arr1, arr2), axis=0))