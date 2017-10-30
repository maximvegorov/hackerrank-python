if __name__ == '__main__':
    n = int(input())
    print(len({input() for i in range(n)}))
