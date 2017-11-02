if __name__ == '__main__':
    _ = int(input())
    counts = dict()
    for room in (int(n) for n in input().split()):
        counts[room] = counts.get(room, 0) + 1
    print(*(room for room, count in counts.items() if count == 1))
