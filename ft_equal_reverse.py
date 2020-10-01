def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_equal_reverse(c):
    z = ft_len(c)
    i = 0
    z = z - 1
    k = 0
    while z - i >= i:
        if c[z - i] == c[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        return False
    return True
