def ft_len(a):
    b = 0
    for i in a:
        b += 1

    return b


def ft_find_str(str1, str2):
    if str2 in str1:
        for i in range(ft_len(str1)):
            for j in str2:
                if str1[i] == j:
                    if str1[i:ft_len(str2) + i] == str2:
                        return i
    return -1
