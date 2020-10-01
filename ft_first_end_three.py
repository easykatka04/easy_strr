def ft_len(a):
    b = 0
    for i in a:
        b += 1
    return (b)


def ft_first_end_three(a):
    if ft_len(a) > 5:
        return (a[:3] + a[-3:])
    else:
        return (a[0] * ft_len(a))
