def ft_len(str):
    b = 0
    for i in str:
        b += 1

    return b


def ft_slice_str(string, start, stop):
    g = ''
    if stop > ft_len(string):
        for i in range(1, ft_len(string)):
            g += string[i]
        return g
    for i in range(start-1, stop):
        g += string[i]
    return g
