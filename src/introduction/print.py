if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        s = ''
        r = i
        while r != 0:
            s += str(r % 10)
            r //= 10
        print(s[::-1], end='')
