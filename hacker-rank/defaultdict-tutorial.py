# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n, m = map(int, input().split())
# A = [input() for _ in range(n)]
# N = [input() for _ in range(m)]

# for i in N:
#     num_list = [m + 1 for m in range(len(A)) if i == A[m]]
#     if(len(num_list) > 0):
#         print(*num_list, sep=' ')
#     else:
#         print('-1')

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))

for _ in range(m):
    print(' '.join(d[input()]) or -1)
