if __name__ == '__main__':
    # N = int(input())
    list = []
    N = 12
    commands = [
"insert 0 5",
"insert 1 10",
"insert 0 6",
"print",
"remove 6",
"append 9",
"append 1",
"sort",
"print",
"pop",
"reverse",
"print"
    ]

    # for _ in range(N):
    for command_line in commands:
        # command, *arguments = input().split()
        command, *arguments = command_line.split()

        if command == "insert":
            list.insert(int(arguments[0]), int(arguments[1]))
        elif command == "print":
            print(list)
        elif command == "remove":
            list.remove(int(arguments[0]))
        elif command == "append":
            list.append(int(arguments[0]))
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        else:
            pass

# # expected output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]