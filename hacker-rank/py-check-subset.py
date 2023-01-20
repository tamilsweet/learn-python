# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for _ in range(T):
    a_count = int(input())
    A = list(map(int, input().split()))
    b_count = int(input())
    B = list(map(int, input().split()))
    subset = 'True'
    for a in A:
        if a not in B:
            subset = 'False'
            break
    print(subset)