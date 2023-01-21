# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S, k, i = input(), input(), 0

if re.search(k, S):
    while i + len(k) < len(S):
        m = re.search(k, S[i:])
        if m:
            print("({0}, {1})".format(i + m.start(), i + m.end() - 1))
            i += m.start() + 1
        else: break
else: print((-1, -1))