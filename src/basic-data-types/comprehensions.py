if __name__ == '__main__':
    x_max = int(input())
    y_max = int(input())
    z_max = int(input())
    n = int(input())
    print(
        sorted([
            [x, y, z]
            for x in range(x_max + 1)
            for y in range(y_max + 1)
            for z in range(z_max + 1)
            if (x + y + z != n)]))
