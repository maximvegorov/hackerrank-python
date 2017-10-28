if __name__ == '__main__':
    n = int(input())
    l = list()
    for i in range(n):
        name = input()
        score = float(input())
        l.append([name, score])
    second_lower = sorted({p[1] for p in l}, reverse=True)[-2]
    print(*sorted((p[0] for p in l if abs(p[1] - second_lower) < 1e-6)), sep='\n')
