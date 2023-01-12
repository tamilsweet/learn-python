# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set([input() for i in range(n)])
print(len(countries))