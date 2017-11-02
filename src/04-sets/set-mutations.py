if __name__ == '__main__':
    _ = input()
    S = {int(n) for n in input().split()}
    for i in range(int(input())):
        op, _ = input().split()
        arg = (int(n) for n in input().split())
        if op == 'update':
            S.update(arg)
        elif op == 'intersection_update':
            S.intersection_update(arg)
        elif op == 'difference_update':
            S.difference_update(arg)
        elif op == 'symmetric_difference_update':
            S.symmetric_difference_update(arg)
        else:
            raise AssertionError
    print(sum(S))
