# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
text = '\n'.join([input() for _ in range(N)])
text = re.sub(r"(?<= )&&(?= )", "and", text)
text = re.sub(r"(?<= )\|\|(?= )", "or", text)
print(text)