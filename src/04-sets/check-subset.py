if __name__ == '__main__':
    test_count = int(input())
    for test_no in range(test_count):
        _ = int(input())
        A = set(input().split())
        _ = int(input())
        B = set(input().split())
        print(A <= B)
