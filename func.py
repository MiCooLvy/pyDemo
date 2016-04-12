def cp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


print cp(2, 2)


def pow(x, n=2):
    m = 1
    for i in range(n):
        m *= x
    return m


print pow(5), pow(5, 3)

print range(20)
