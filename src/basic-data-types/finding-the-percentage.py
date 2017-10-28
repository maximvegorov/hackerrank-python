if __name__ == '__main__':
    n = int(input())
    d = dict()
    for i in range(n):
        n, *p = input().split()
        d[n] = sum((float(s) for s in p)) / 3
    print('%.2f' % d[input()])
