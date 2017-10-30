if __name__ == '__main__':
    A = set(input().split())
    for _ in range(int(input())):
        B = set(input().split())
        if not A > B:
            print(False)
            break
    else:
        print(True)
