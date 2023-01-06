if __name__ == '__main__':
  x = 3
  y = 2
  z = 1
  n = 3

#   list = []
#   for i in range(x+1):
#       for j in range(y+1):
#           for k in range(z+1):
#               if( i + j + k != n):
#                   list.append([i, j, k])
#   print(list)

  list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
  print(list)
