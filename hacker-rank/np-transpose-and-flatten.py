import numpy

N, M = map(int, input().split())
arr = []
for i in range(N):
   arr.append(list(map(int, input().split())))
   
narr = numpy.array(arr)
print(numpy.transpose(narr))
print(narr.flatten())