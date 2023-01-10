def print_formatted(number):
    # your code goes here
    pad = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        d = str(i).rjust(pad)
        o = str(oct(i)[2:]).rjust(pad)
        h = str(hex(i)[2:]).upper().rjust(pad)
        b = str(bin(i)[2:]).rjust(pad)
        print(d, o, h, b)
    return  
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)