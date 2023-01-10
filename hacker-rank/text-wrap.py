import textwrap

def wrap(string: str, max_width):
    # return "\n".join(textwrap.wrap(string, max_width))

    # str = ""
    # for i in range(0, len(string), max_width):
    #     str = str + string[i:i+max_width] + '\n'
    # return str

    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)