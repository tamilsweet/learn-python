def print_rangoli(size):
    # your code goes here
    line_width = size * 4 - 3
    text = "abcdefghijklmnopqrstuvwxyz"
    range_list = list(range(1,size+1))+list(range(size-1,0,-1))
    for i in range_list:
        char = '-'.join([text[size-j] for j in range(1, i+1)] + [text[size-k+1] for k in range(i, 1, -1)])
        print(char.center(line_width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)