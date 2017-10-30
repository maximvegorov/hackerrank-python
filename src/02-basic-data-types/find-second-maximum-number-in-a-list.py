if __name__ == '__main__':
    _ = int(input())
    print(sorted({int(s) for s in input().split()})[-2])