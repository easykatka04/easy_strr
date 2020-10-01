def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_reverse_str(n):
    v = ''
    for i in range(-1, -ft_len(n) - 1, -1):
        v += n[i]
    return v
