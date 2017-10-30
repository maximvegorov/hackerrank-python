if __name__ == '__main__':
    _ = int(input())
    M = {int(n) for n in input().split()}
    _ = int(input())
    N = {int(n) for n in input().split()}
    print(*sorted(M ^ N), sep='\n')
