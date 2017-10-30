def happyness(n, A, B):
    if n in A:
        return 1
    elif n in B:
        return -1
    else:
        return 0


if __name__ == '__main__':
    _ = input()
    M = [int(n) for n in input().split()]
    A = {int(n) for n in input().split()}
    B = {int(n) for n in input().split()}
    print(sum((happyness(n, A, B) for n in M)))
