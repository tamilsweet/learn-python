# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
shoes = Counter(map(int, input().split()))
N = int(input())

earned = 0

for _ in range(N):
    size, price = map(int, input().split())
    if(shoes[size] > 0):
        earned += price
        shoes.subtract([size])

print(earned)