# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K = int(input())
room_list = list(map(int, input().split()))
print(Counter(room_list).most_common()[-1][0])