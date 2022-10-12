def rev(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(rev(a, b))
