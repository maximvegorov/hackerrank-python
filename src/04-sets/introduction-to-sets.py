if __name__ == '__main__':
    _ = int(input())
    s = {int(n) for n in input().split()}
    print(sum(s) / len(s))
