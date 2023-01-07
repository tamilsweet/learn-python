# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(numpy.inner(A, B))
print(numpy.outer(A, B))
