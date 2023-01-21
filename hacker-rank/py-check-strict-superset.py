# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
result = 'True'
for _ in range(n):
    if not A.issuperset(set(map(int, input().split()))):
        result = 'False'
        break

print(result)