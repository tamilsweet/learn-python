# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

print(numpy.dot(A, B))
