if __name__ == '__main__':
    _ = int(input())
    s = {int(n) for n in input().split()}
    m = int(input())
    for i in range(m):
        cmd, *args = input().split()
        if cmd == 'pop':
            s.pop()
        elif cmd == 'remove':
            s.remove(int(args[0]))
        elif cmd == 'discard':
            s.discard(int(args[0]))
        else:
            raise AssertionError
    print(sum(s))
