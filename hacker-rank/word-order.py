# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
words = OrderedDict()
for _ in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())

##############

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
words = Counter([input() for _ in range(n)])
print(len(words))
print(*words.values())