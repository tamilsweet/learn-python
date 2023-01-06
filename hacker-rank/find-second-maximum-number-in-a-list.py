if __name__ == '__main__':
    n = 5 #int(input())
    arr = [2, 3, 6, 6, 5] # map(int, input().split())
    arr.sort(reverse=True)
    first = arr[0]
    for score in arr:
      if score < first:
        print(score)
        break