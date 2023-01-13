# Enter your code here. Read input from STDIN. Print output to STDOUT
# from itertools import permutations
# S, k = input().split()
# combinations = sorted([''.join(i) for i in list(permutations(S, int(k)))])
# for i in combinations:
#     print(i)

from itertools import permutations
S, k = input().split()
print(*[''.join(i) for i in permutations(sorted(S), int(k))], sep='\n')