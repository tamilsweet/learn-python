# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

P = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(P, x))
