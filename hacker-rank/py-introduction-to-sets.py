def average(array):
    # your code goes here
    numberset = set(array)
    return sum(numberset) / len(numberset)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)