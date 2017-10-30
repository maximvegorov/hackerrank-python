if __name__ == '__main__':
    _ = input()
    s1 = {int(n) for n in input().split()}
    _ = input()
    s2 = {int(n) for n in input().split()}
    print(len(s1 - s2))
