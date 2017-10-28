if __name__ == '__main__':
    l = list()
    for i in range(int(input())):
        cmd, *args = input().split()
        if cmd == 'insert':
            l.insert(int(args[0]), args[1])
        elif cmd == 'print':
            print(l)
        elif cmd == 'remove':
            if l.count(args[0]) > 0:
                l.remove(args[0])
        elif cmd == 'append':
            l.append(args[0])
        elif cmd == 'sort':
            l.sort()
        elif cmd == 'pop':
            if len(l) > 0:
                l.pop()
        elif cmd == 'reverse':
            l.reverse()
        else:
            raise AssertionError()
