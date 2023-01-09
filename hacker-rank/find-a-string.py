def count_substring(string, sub_string):
    start = 0
    count = 0
    while True:
        start = string.find(sub_string, start)
        if start == -1:
            break
        else:
            start = start + 1
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)