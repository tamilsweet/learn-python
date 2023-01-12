n = int(input())
s = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    command = input().split()
    try:
        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            s.remove(int(command[1]))
        elif command[0] == "discard":
            s.discard(int(command[1]))
    except KeyError:
        pass
           
print(sum(s))