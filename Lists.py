if __name__ == '__main__':
    N = int(input())
    list1 = []
    for commandLine in range(0,N):
        commandLine = input().split()
        command = str(commandLine[0])
        commandLine.extend([1,1])
        index = int(commandLine[1])
        elementX = int(commandLine[2])
        #for i in commandLine:
        #   if commandLine[1] == None:

        for command in commandLine:
            if command == 'insert':
                list1.insert(index, elementX)
            elif command == 'print':
                print(list1)
            elif command == 'remove':
                list1.remove(int(commandLine[1]))
            elif command == 'append':
                list1.append(int(commandLine[1]))
            elif command == 'sort':
                list1.sort()
            elif command == 'pop':
                list1.pop()
            elif command == 'reverse':
                list1.reverse()