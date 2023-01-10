# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
# -- INPUT
# 7, 21

# -- OUTPUT
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# 0 = 3 0 + 3
# 1 = 9 6 + 3
# 2 = 15 12 + 3
# 3 = 21 18 + 3

# M = M // 2
# pattern = ".|."
# for line in range(N//2):
#     print("-" * (M - line * 3 - 1) + pattern * (line * 2 + 1) + "-" * (M - line * 3 - 1))

# print("-" * (M - 3) + "WELCOME" + "-" * (M - 3))

# for line in range(N//2 - 1, -1, -1):
#     print("-" * (M - line * 3 - 1) + pattern * (line * 2 + 1) + "-" * (M - line * 3 - 1))


pattern = ".|."
for line in range(N//2):
  print((pattern * (line * 2 + 1)).center(M, '-'))
print("WELCOME".center(M, '-'))
for line in range(N//2 - 1, -1, -1):
  print((pattern * (line * 2 + 1)).center(M, '-'))